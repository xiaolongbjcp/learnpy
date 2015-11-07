

from wsgiref.simple_server import make_server
from ex31_hello import application

server_http = make_server('', 8002, application)

server_http.serve_forever()
