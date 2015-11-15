

import socket
import threading
import time, random
import json
from multiprocessing import Process, Queue

# gUserList = {Name: (Addr, Sock)}
gUserList = {}


gConnList = {}



def fdecode(s):
	return s.decode('utf-8')



def login_handler(sock, addr, username = ''):
	global gUserList
	gUserList[username] = (addr, sock)
	print (gUserList)

	gConnList[addr] = (username, sock)




def conn_handler(sock, addr, name_source = '' ,name_destin = ''):

	if name_destin in gUserList.keys():

		sub_port = '8888'

		print ('handling...')
		name_source = name_source
		addr_source = gUserList[name_source][0]
		sock_source = gUserList[name_source][1]

		sourceDict = {}
		sourceDict[name_source] = (addr_source, sub_port)
		print ('sourceDict:',sourceDict)

		name_destin = name_destin
		addr_destin = gUserList[name_destin][0]
		sock_destin = gUserList[name_destin][1]

		destinDict = {}
		destinDict[name_destin] = (addr_destin, sub_port)
		print ('destinDict', destinDict)

		sock_source.send(json.dumps(sourceDict).encode('utf-8'))
		sock_destin.send(json.dumps(destinDict).encode('utf-8'))



		gMessage = 'invention send!'.encode('utf-8')
		sock.send(gMessage)

	else:
		gMessage = ('No "%s" exist!' % name_destin).encode('utf-8')
		sock.send(gMessage)



def tSRecv_thread(sock, addr):

	global gUserList

	# Name for subprocess
	gProcessName = None


	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')

	while True:

		data_recv = fdecode(sock.recv(1024))			

		if data_recv[0:7] == '[login]':
			print ('%s login...'% data_recv[7:])
			gProcessName = data_recv[7:]
			login_handler(sock, addr, data_recv[7:])

		elif data_recv[0:6] == '[list]':
			gMessage = b'[list]' + json.dumps(gUserList).encode('utf-8')

			sock.send(gMessage)

		elif data_recv[0:6] == '[conn]':
			name_destin = data_recv[7:]
			conn_handler(sock, addr, gProcessName, name_destin)
			

		elif data_recv == 'exit':
			break

		else:
			gMessage = data_recv.encode('utf-8')

			sock.send(gMessage)
	

		
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9998))

s.listen(5)
print('Waiting for connection...')


while True:
	
	sock, addr = s.accept()
	print ('sock:', sock)
	print ('addr:', type(addr))
	print ('Request from:',addr)
	gConnList[addr] = ''
	
	# pSRecv = Process(target = pSRecv_Process, args = (sock, addr))
	tSRecv = threading.Thread(target=tSRecv_thread, args=(sock, addr))

	tSRecv.start()

