

import socket

s_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr_server = ('127.0.0.1', 9997)

s_server.bind(addr_server)

data, addr_client = s_server.recvfrom(1024)

print ('Rceive data: %s\n\tfrom:' %data, addr_client)

s_server.sendto(b'Hello, this message is from udp-server!', addr_client)

# s_server.close()
