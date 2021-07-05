import os
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

PORT = 3000

ROUTES = [
    ("/", "index.html"),
    ("/oauth/kakao/callback", "kakao_callback.html"),
    ("/oauth/google/callback", "google_callback.html"),
]

web_dir = os.path.join(os.path.dirname(__file__), "web")
os.chdir(web_dir)

class CustomSimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        root = os.getcwd()

#         print(f"path: {path}")
        for _path, root_dir in ROUTES:
            if path.startswith(_path):
                path = path[len(_path):]
                root = root_dir
                break

        print(f"path: {path}")
        return os.path.join(web_dir, path)

    def do_GET(self):
        print(self.path)
        for _path, _html in ROUTES:
            if self.path.split("?")[0] == _path:
                self.path = _html
                return SimpleHTTPRequestHandler.do_GET(self)
        
        return super(CustomSimpleHTTPRequestHandler, self).do_GET()



httpd = HTTPServer(("", PORT), CustomSimpleHTTPRequestHandler)
httpd.serve_forever()
