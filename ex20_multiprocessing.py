

import os
from multiprocessing import Process

def proc_handler(name):
	print ('This proc_handler, and the name is', name)
	print ('This process id in hanlder is', os.getpid(), '\n')

p = Process(target = proc_handler, args=('p1',))
print ('This process id before booting is', os.getpid(), '\n')
p.start()
p.join()

print ('The end...')