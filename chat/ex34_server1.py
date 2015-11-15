

import socket
import threading
import time, random
import json

gMessage = None
gUserList = {}

def login_handler(username, addr):
	global gUserList
	gUserList[username] = addr

def fdecode(s):
	return s.decode('utf-8')



def tSRecv_thread(sock, addr):

	global gMessage
	global gUserList
	lock = threading.Lock()

	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')

	while True:

		data = sock.recv(1024)
		lock.acquire()
		try:

			if fdecode(data)[0:7] == '[login]':
				print ('%s login...'% data.decode('utf-8')[7:])
				login_handler(fdecode(data)[7:], addr)

			elif fdecode(data)[0:7] == '[list]':
				gMessage = b'[list]' + json.dumps(gUserList).encode('utf-8')

			elif not data or fdecode(data) == 'exit':
				break

			else:
				gMessage = data
		
		finally:
			if (gMessage):
				sock.send(b'sever received:'+gMessage)
				gMessage = None
			lock.release()

		
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')

while True:
	
	sock, addr = s.accept()
	print ('sock:', type(sock))
	print ('addr:', type(addr))
	print ('Request from:',addr)
	
	tSRecv = threading.Thread(target=tSRecv_thread, args=(sock, addr))

	tSRecv.start()

