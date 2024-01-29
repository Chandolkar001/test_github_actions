from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        # data = json.loads(body)
        data = body
        print(body)

        # Process the received data
        response = {'status': 'success', 'message': 'POST request received', 'data': data}
        response_json = json.dumps(response).encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', len(response_json))
        self.end_headers()
        self.wfile.write(response_json)

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()