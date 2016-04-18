
from multiprocessing import Pool
import os
import random, time

def handler1(i, no):
	print ('this order is:', i)	
	print ('I am:', os.getpid())
	print ('parent is:', no)
	print ('parent I get is:', os.getppid())
	print ('sleeping...')
	time.sleep(random.random()*4)
	print (os.getpid(),'waked up!')


print ('Now we are in process:', os.getpid())

p = Pool(4)

for i in range(3):
	p.apply_async(handler1, args=(i, os.getpid()))

print ('Configuraion done!')

for i in range(5):
	print (i)
	# handler1(i, 998)

p.close()
for i in range(3):
	print (i)
p.join()
print ('Game over!')

import subprocess

p2 = subprocess.Popen('python', stdin=subprocess.PIPE, stderr=subprocess.PIPE)
for i in range(9):
	print (i)
output, err = p2.communicate(b"print ('hello!')")
print (output)


def handler3(q):
	print ('writing...')
	for v in range(5):
		q.put(v)
		print (v,' written!')
		time.sleep(random.random())

def handler4(q):
	print ('reading..')
	while (True):
		v = q.get(True)
		print ('get the key is:', v)


from multiprocessing import Process, Queue
q = Queue()
pw = Process(target = handler3, args=(q,))
pr = Process(target = handler4, args=(q,))
pr.start()
pw.start()
# pr.start()
pw.join()
pr.terminate()