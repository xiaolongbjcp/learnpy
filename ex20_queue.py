

import os, time, random
from multiprocessing import Process, Queue

def proc_write_handler(q):
	print ('This is write handler to put value into queue...')
	for i in range(16):
		q.put(i)
		print ('Put the value (%s) into queue.' %i)
		time.sleep(random.random())

def proc_read_handler(q):
	print ('This is read handler to read value from queue...')
	while True:
		value = q.get(True)
		print ('Get value from queue:', value)

q = Queue()

pw = Process(target = proc_write_handler, args = (q,))
pr = Process(target = proc_read_handler, args = (q,))

pw.start()
pr.start()

pw.join()
pr.terminate()

