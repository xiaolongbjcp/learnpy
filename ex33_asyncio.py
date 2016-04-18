

import asyncio
import threading

@asyncio.coroutine
def hello1():
	print ('Hello world1! (%s)' % threading.currentThread())

	r = yield from asyncio.sleep(10)
	print ('Hello again1! (%s)'% threading.currentThread())

@asyncio.coroutine
def hello2():
	print ('Hello world2! (%s)' % threading.currentThread())

	r = yield from asyncio.sleep(9)
	print ('Hello again2! (%s)' % threading.currentThread())

@asyncio.coroutine
def hello3():
	print ('Hello world3! (%s)' % threading.currentThread())

	r = yield from asyncio.sleep(9)
	print ('Hello again3! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()

tasks = [hello1(), hello2(), hello3(), hello1(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()


