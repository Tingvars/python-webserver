import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("this is working - Thora")
        http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8080
Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving the website at port # ", PORT)
    httpd.serve_forever()