

import socket
import threading
import json

gUserList = {}

def fdecode(s):
	return s.decode('utf-8')

def tRecv_thread(sock):

	global gUserList

	while True:

		data_recv = fdecode(sock.recv(1024))

		if data_recv[0:6] == '[list]':
			gUserList = json.loads(data_recv[6:])
			print (gUserList)
		else:			
			print (data_recv)

def tSend_thread(sock):

	# print('Accept new connection...')	
	# for data in [b'Michael', b'Tracy', b'Sarah']:
	# 	sock.send(data)

	while True:
		data2 = input()
		if data2 == 'exit':
			print ('Bye!')
			break
		elif data2 == '_list':
			sock.send('[list]'.encode('utf-8'))
		elif data2[0:5] == '_conn':
			sock.send(('[conn]'+data2[5:]).encode('utf-8'))
		else:
			sock.send(data2.encode('utf-8'))

	sock.send(b'exit')


def login(s):

	username = input('Please input your name: ')
		
	s.send(('[login]'+username).encode('utf-8'))
	
	print(s.recv(1024).decode('utf-8'))


sEnd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sEnd.connect(('127.0.0.1', 9998))

print('Waiting for connection...')

login(sEnd)
	
tRecv = threading.Thread(target=tRecv_thread, args=(sEnd,))
tSend = threading.Thread(target=tSend_thread, args=(sEnd,))
tRecv.start()
tSend.start()


