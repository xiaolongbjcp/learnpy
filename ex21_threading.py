

import threading
import time, random
import os

def thrd_handler(name):
	print ('thread (%s) starts in process(%s)' % (name, os.getpid()))
	time.sleep(random.random())
	print ('thread (%s) finished in process(%s)' % (name, os.getpid()))

t = threading.Thread (target = thrd_handler, name = 'thread in ex21', args = ('test0',) )
print ('Pid is %s before.' % os.getpid())
t.start()
t.join()
