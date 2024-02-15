# Asyncio does not reliably work all in jupyter environments
import aiohttp
import aiofiles
import asyncio
import bs4
from datetime import datetime
from pathlib import Path
import requests
import ssl
import certifi

start_time = datetime.utcnow()
sslcontext = ssl.create_default_context(cafile=certifi.where())
output_folder = (
    Path.cwd().parent.parent.parent / "processing" / "nro_declassified" / "pdfs"
)
base_url = "https://www.nro.gov"
r = requests.get(
    f"{base_url}/foia-home/foia-declassified-major-nro-programs-and-projects/CAL-Library-Listing/"
)
soup = bs4.BeautifulSoup(r.text, "lxml")
rows = soup.find_all("tr")  # find the table rows

tasks = []  # prepare tasks -> ultimately should be a list of dicts in format url_to_get: file_name_to_save_resp_as
for row in rows:
    cells = row.find_all("td")
    if len(cells) == 7:  # there are other tables on the page but ours is 7 cells wide
        id = cells[0].text
        link = cells[1].find("a")
        if link is not None:
            link = link.get("href")
        name = cells[2].text
        for char in '<>:"/\|?*,.-':  # not allowed in a windows file name
            name = name.replace(char, "")
        name = name[:60]  # low value bcuz there is also a windows length concern
        date = cells[3].text
        date = date.replace("(Estimated)", "")  # text randomly included with date
        date = date.strip()
        try:
            date = datetime.strptime(date, "%m/%d/%Y").date().isoformat()
        except Exception:
            date = (
                datetime.utcnow().date().isoformat()
            )  # unparseable or otherwise unavailable - just set todays date
        if link is not None:
            if "?ver=" in link:  # one cell has URL parameters that don't work
                link = link.split("?ver=")[0]
            link = link.strip()
            tasks.append(
                {
                    "url": f"{base_url}{link}",
                    "file_name": output_folder / f"{date}_{name}_{id}.pdf",
                }
            )


async def download_pdf(session, url, file_name):
    try:
        async with session.get(url, ssl=sslcontext) as resp:
            content = await resp.read()
            return content
    except aiohttp.ClientConnectorError as e:
        print(f"Connection Error: {str(2)}", str(e))
        print(f"\n\nURL: {url} failed to download {file_name}")
        return b""


async def write_pdf(session, url, file_name):
    content = await download_pdf(session, url, file_name)
    async with aiofiles.open(file_name, "wb") as f:
        await f.write(content)


async def bulk_crawl(urls_dict):
    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []
        for task_dict in urls_dict:
            tasks.append(write_pdf(session, task_dict["url"], task_dict["file_name"]))
        await asyncio.gather(*tasks)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(bulk_crawl(tasks))
print(
    f"Executed {len(tasks)} URL fetch tasks. Run time: {datetime.utcnow() - start_time}"
)
