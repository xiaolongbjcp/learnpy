

import socket
import threading
import time, random

gMessage = None

def tSRecv_thread(sock, addr):

	global gMessage

	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		if not data or data.decode('utf-8') == 'exit':
			break
		else:
			gMessage = data
	# sock.close()
	print('Connection from %s:%s closed.' % addr)
	

def tSSend_thread(sock, addr):

	global gMessage

	while True:
		if (gMessage):
			sock.send(('Hello, %s!' % gMessage.decode('utf-8')).encode('utf-8'))
			gMessage = None
		
	
	




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9998))

s.listen(5)
print('Waiting for connection...')

while True:
	
	sock, addr = s.accept()
	print ('sock:', type(sock))
	print ('addr:', type(addr))
	print ('Request from:',addr)
	
	tSRecv = threading.Thread(target=tSRecv_thread, args=(sock, addr))
	tSSend = threading.Thread(target=tSSend_thread, args=(sock, addr))

	tSRecv.start()
	tSSend.start()

