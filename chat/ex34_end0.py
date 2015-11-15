

import socket
import threading


def tRecv_thread(sock):
	while True:
		print(sock.recv(1024).decode('utf-8'))

def tSend_thread(sock):

	# print('Accept new connection...')	
	# for data in [b'Michael', b'Tracy', b'Sarah']:
	# 	sock.send(data)

	while True:
		data2 = input()
		if data2 == 'exit':
			print ('Bye!')
			break
		else:
			sock.send(data2.encode('utf-8'))

	sock.send(b'exit')
	# sock.close()
	quit()




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9998))

print('Waiting for connection...')
	
tRecv = threading.Thread(target=tRecv_thread, args=(s,))
tSend = threading.Thread(target=tSend_thread, args=(s,))
tRecv.start()
tSend.start()


