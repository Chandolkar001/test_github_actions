from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(body)
        print(data)
        

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
