

import socket

s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr_server = ('127.0.0.1', 9997)

data = b'Hello udp server!'

s_client.sendto(data, addr_server)

data = s_client.recv(1024).decode('utf-8')

print (data)

s_client.close()
