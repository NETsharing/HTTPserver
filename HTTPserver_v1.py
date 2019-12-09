"""
####################################################################################################################
Тестовое задание: надо написать HTTP-сервер, который при GET-запросе будет возвращать число.
При первом запросе это должен быть 0, при втором - 1, третий - 2 и т.д
####################################################################################################################
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
calls = 0
class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        global calls
        calls +=1
        bitecode = str(calls).encode()
        self.wfile.write(b"<body><p>%s</p></body>" % bitecode)


serv = HTTPServer(("localhost", 80), HttpProcessor)
serv.serve_forever()