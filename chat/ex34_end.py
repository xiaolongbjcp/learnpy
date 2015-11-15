

import os
import json
import socket
import threading
import time

from multiprocessing import Process

# Name
gUserList = {}

# Name: Sock
gSockList = {}

# Name
gCurrentDest = None

gData_In = None

gServerPort = 9999

def fdecode(s):
	return s.decode('utf-8')


def conn_server_process_handler(recv_data):
	global gCurrentDest
	print ('preparing server for:',recv_data)
	# {"xiaolong": [["127.0.0.1", 34787], "8888"]}
	conn_port = int(recv_data.split('"')[5])


	conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conn_sock.bind(('127.0.0.1', conn_port))
	conn_sock.listen(5)

	accp_sock, accp_addr = conn_sock.accept()
	print ('accp_sock:', accp_sock)
	print ('Request from:',accp_addr)

	gSockList[recv_data.split('"')[1]] = accp_sock
	gCurrentDest = recv_data.split('"')[1]

	tss = threading.Thread(target=tRecv_thread, args=(accp_sock,))
	tss.start()


def conn_client_process_handler(recv_data):
	global gCurrentDest

	print ('preparing client for:',recv_data)
	conn_port = int(recv_data.split('"')[5])
	conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	conn_sock.connect(('127.0.0.1', conn_port))

	gSockList[recv_data.split('"')[1]] = conn_sock	
	gCurrentDest = recv_data.split('"')[1]
	
	tss = threading.Thread(target=tRecv_thread, args=(conn_sock,))
	tss.start()




def conn_handler(recv_data):

	if recv_data[0:3] == '[S]':
		print ('run a server Process...')
		# print (recv_data[3:])
		conn_server_process_handler(recv_data)
		
	
	elif recv_data[0:3] == '[C]':
		print ('run a client Process...')
		# print (recv_data[3:])
		time.sleep(0.1)
		conn_client_process_handler(recv_data)
		


def tRecv_thread(sock):

	global gUserList
	global gCurrentDest
	while True:

		data_recv = fdecode(sock.recv(1024))

		if data_recv[0:6] == '[list]':
			gUserList = json.loads(data_recv[6:])
			print (gUserList)

		elif data_recv[0:6] == '[conn]':
			conn_handler(data_recv[6:])

		elif data_recv[0:6] == '[exit]':
			print (data_recv)
			gCurrentDest = 'server'
			break

		else:			
			print (data_recv)
	sock.close()


def tSend_handler(data_in, sock):
	sock.send(data_in)


def input_handler(gData_In, sock):
	global gCurrentDest

	if gData_In[0:6] == '_login':

		tSend_handler(('[login]'+gData_In[6:]).encode('utf-8'), sock)

	elif gData_In == '_list':

		tSend_handler('[list]'.encode('utf-8'), sock)

	elif gData_In[0:5] == '_conn':

		if gData_In == '_conn':
			print (gSockList.keys())
		else:
			tSend_handler(('[conn]'+gData_In[5:]).encode('utf-8'), sock)

	elif gData_In[0:7] == '_switch':
		print ('ready to switch')
		if gData_In[8:] in gSockList.keys():
			print ('switch to', gData_In[8:])
			gCurrentDest = gData_In[8:]
		else:
			print ('the client does not exist!')

	else:
		tSend_handler(gData_In.encode('utf-8'), sock)

def tInput_handler(sock):
	global gCurrentDest

	while True:
		gData_In = input()

		if gData_In == '_exit':
			print ('Bye!')

			tSend_handler('[exit]'.encode('utf-8'), gSockList[gCurrentDest])
			
			gSockList[gCurrentDest].close()
			
			if gCurrentDest != 'server':
				gCurrentDest = 'server'

			else:
				break

		input_handler(gData_In, gSockList[gCurrentDest])
	print ('input end...')
		


sEnd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sEnd.connect(('127.0.0.1', gServerPort))

gSockList['server'] = sEnd

gCurrentDest = 'server'

print('Waiting for connection...')

tRecv = threading.Thread(target=tRecv_thread, args=(sEnd,))
tRecv.start()

tInput = threading.Thread(target=tInput_handler, args=(gSockList[gCurrentDest],))
tInput.start()


tRecv.join()
tInput.join()
print ('end!!!')
