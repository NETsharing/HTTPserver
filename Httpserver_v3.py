from http.server import BaseHTTPRequestHandler, HTTPServer
calls = 0
def httprequests_call(http_method):
    def decorated(*args, **kwargs):
        global calls
        calls += 1
        return http_method(*args, **kwargs)
    return decorated

class HttpProcessor(BaseHTTPRequestHandler):
    @httprequests_call
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        z = str(calls).encode()
        self.wfile.write(b"<body><p>%s</p></body>" % z)


serv = HTTPServer(("localhost", 80), HttpProcessor)
serv.serve_forever()