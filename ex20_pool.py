

from multiprocessing import Pool
import os, time, random

def proc_handler(name):
	print ('This child process\'s name is', name)
	# print ('Pid in child %s is %s' %(name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*7)
	end = time.time()
	print ('Task %s runs %0.3f seconds.\n' % (name ,end - start))


p = Pool(20)

for i in range(21):
	p.apply_async(proc_handler, args = (('test'+str(i)),))

print ('Running...')

p.close()
p.join()
print ('All pass...')