from dash import html
from datetime import datetime
import dash_bootstrap_components as dbc

name = "Holston Mountain Plane Crashes"
# The below format is intended to help simplify the development and addition of content
# for ach accordion item, if it provided a date of the crash in iso-format it will be sorted by date
army_l20_1960 = dbc.AccordionItem(
    html.Div(
        children=[
            html.P(
                [
                    "According to the ",
                    html.A(
                        "Johnson City Press-Chronicle", href="/#army_l20_1960_newspaper"
                    ),
                    ", an Army L20 crashed into the top of Cove Ridge in the Holston Mountains at 00:30 EST.",
                    " A FOIA request was submitted to the Army and may be independently ",
                    html.A(
                        "downloaded and reviewed.",
                        href="/data/1960_army_l20_foia.pdf",
                        download="1960_army_l20_foia.pdf",
                    ),
                    " Within the report, there are topographic scans of the area, several pictures taken from the perspective of the crash site, and detailed radio traffic surrounding the incident.",
                ]
            ),
            html.P(
                [
                    "On page 61, the crash site is described as",
                    html.Em(
                        html.B(
                            " 'on a 2100 foot hill, ten miles from Tri City Airport on a heading of 102 degrees or 4 miles from the Tri City Omni on a heading of 270 degrees or 1 mile north of the V16-V185E Airways'"
                        )
                    ),
                    " and ",
                    html.Em(
                        html.B(
                            "' [the plane] struck the trees 154 feet below the crest of the hill in a wing level'"
                        )
                    ),
                    ". ",
                ]
            ),
        ]
    ),
    title="Dec 17, 1960, Army L-20 (SN 54-41671)",
    id=datetime(1960, 12, 17).date().isoformat(),
)

# the FOIA report here mentions the abandonment at the scene
army_l19_1961 = dbc.AccordionItem(
    html.P(
        children=[
            "On April 5, 1961 at approximately 19:09 EST, an Army L-19D crashed into an unspecified area of Holston Mountain approximately 3600' MSL. ",
            html.A(
                "The statement issued on page 19 of the FOIA request ",
                href="/data/1961_army_l19d_foia.pdf",
            ),
            "states, ",
            html.Em(
                html.B(
                    "'this aircraft was considered demolished to the extent that it was abandoned at crash site.'"
                )
            ),
            html.Br(),
            html.Br(),
            html.P(
                html.I(
                    html.B(
                        "Note: Newspaper articles frequently transpose details between the Army LH-20 and LH-19 crashes. This is likely attributed to both flights being operated by the Army, the crashes occurring in rather short succession, and the similarity of the aircraft involved. Therefore, only the documents contained in the FOIA request and articles immediately preceding the crash were considered authoritative for this crash."
                    )
                ),
                style={"font-size": ".7rem", "text-align": "center"},
            ),
        ]
    ),
    title="Apr 5, 1961, Army L-19D (SN 57-2793)",
    id=datetime(1961, 4, 5).date().isoformat(),
)

dc3_1959 = dbc.AccordionItem(
    html.P(
        children=[
            "On September 8, 1959 at approximately 20:32 EST, a Southeast Airlines Flight (308) struck Holston Mountain (aircraft accident report available at",
            html.A(
                " the Bureau of Transportation Statistics Website),",
                href="https://rosap.ntl.bts.gov/view/dot/33606",
            ),
            " This report includes a very accurate map, which was geolocated in the next step.",
        ]
    ),
    title="Sep 8, 1959, Southwest Airlines DC-3 L-19D (N18941)",
    id=datetime(1959, 9, 8).date().isoformat(),
)

cessna_182 = dbc.AccordionItem(
    html.P(
        children=[
            "On July 3, 1961, a civilian aircraft crashed around 300 yards from the WCYB TV transmitter. ",
            html.A(
                "News footage from investigative personnel shows the immediate area.",
                href="https://curio.lib.virginia.edu/view/uva-lib:2249472",
            ),
            " Separately, the ",
            html.A("Johnson City Press-Chronicle reported ", href="#jcp_cessna_182"),
            "the crash debris was spread over a half mile radius.",
        ]
    ),
    title="Jul 3, 1961, Civilian Operated Cessna 182",
    id=datetime(1961, 7, 3).date().isoformat(),
)

navy_snb = dbc.AccordionItem(
    html.P(
        children=[
            "On February 2, 1958, a Navy SNB crashed into Holston Mountain. A FOIA request needs to be submitted for additional details.",
        ]
    ),
    title="Feb 2, 1958, Navy SNB",
    id=datetime(1958, 2, 2).date().isoformat(),
)

layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("Holston Mountain Plane Crashes"),
        html.Br(),
        html.P(
            "There are significant barriers in the spatial identification of historic plane crashes, such as an overwhelming reliance on the crash record being digitized and searchable. For Holston Mountain crashes, the investigative records are maintained by several different agencies with varying levels of accessibility. To obtain full details for the crashes, it is often required to submit a Freedom of Information Act (FOIA) request, which introduces a significant delay in analysis. After the records are obtained, the quality of the data varies heavily based on crash year and location. This is likely attributable to the labor and costs associated with investigating remote mountainside locations with only foot or aerial access."
        ),
        html.P(
            html.B(
                "The following plane crashes were identified, primarily through keyword searches of digitized newspapers:"
            )
        ),
        dbc.Accordion(
            sorted(
                [army_l20_1960, army_l19_1961, dc3_1959, cessna_182, navy_snb], key=lambda x: x.id
            ),
            start_collapsed=True,
        ),
        html.P(
            "Additional crashes include (1) National Guard Bell OH-58 helicopter in 1998, (2) civilian Operated Beech Bonaza in 2007, (3) civilian operated Cessna 185 in 1981, (4) civilian operated Cessna 172K in 2014, (5) civilian opearted Piper Navho PA31 in 1994 and (6) Air Force RF-4 in 1976. These crashes may be included in the study at a later time; however, the dates for the crashes currently exceed the predicted bounds for the study. The RF-4 is a very likely candidate for inclusion at a later date, due to the known crash site and age of the site."
        ),
    ],
    id="plane-crashes",
    class_name="offset",
)
