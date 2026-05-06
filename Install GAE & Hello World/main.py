from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, App Engine!")

port = 8080
server = HTTPServer(("0.0.0.0", port), Handler)
print("Server running...")
server.serve_forever()