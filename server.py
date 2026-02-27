import http.server
import os

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) or (os.path.isdir(path) and not os.path.exists(os.path.join(path, 'index.html')) and self.path != '/'):
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    http.server.test(HandlerClass=SPAHandler, port=8000)
