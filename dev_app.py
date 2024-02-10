import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    """Restart the server if any files change."""

    def on_any_event(self, event):
        print(f"Restarting due to changes in: {event.src_path}")
        # Terminate the existing server process
        global server_process
        if server_process:
            server_process.terminate()
        # Start a new server process
        server_process = subprocess.Popen(["waitress-serve", "--listen=127.0.0.1:8050", "app:server"])

if __name__ == "__main__":
    path = "."  # Path to watch for changes
    handler = ChangeHandler()
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    # Initial server start
    server_process = subprocess.Popen(["waitress-serve", "--listen=127.0.0.1:8050", "app:server"])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
