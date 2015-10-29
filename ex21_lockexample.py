

#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(900000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('threading:',balance)


print ('------------multiprocessing------------')

print ('balance is reset to 0.')
balance = 0


from multiprocessing import Process
import multiprocessing

import os

def proc_handler(name, n):
	print ('Process (%s) starts...' % os.getpid())
	for i in range (9000000):
		change_it(n)

p1 = Process (target = proc_handler, args = ('p1', 5))
p2 = Process (target = proc_handler, args = ('p2', 8))

p1.start()
p2.start()

p1.join()
print ('P1:', balance)
p2.join()
print ('P2:', balance)
print ('cpu count is ', multiprocessing.cpu_count())
