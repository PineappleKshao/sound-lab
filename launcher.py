"""Local-only launcher; serves files without uploading any audio."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import threading
import webbrowser

folder = Path(__file__).resolve().parent
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(folder)))
url = f'http://127.0.0.1:{server.server_port}/'
print(f'\nSound Lab is running at {url}\nKeep this window open. Press Control-C to stop.\n', flush=True)
threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
