

import asyncio
import threading

@asyncio.coroutine
def hello():
	print ('Hello world! (%s)' % threading.currentThread())

	r = yield from asyncio.sleep(10)
	print ('Hello again! (%s)'% threading.currentThread())

@asyncio.coroutine
def hello2():
	print ('Hello world2! (%s)' % threading.currentThread())

	r = yield from asyncio.sleep(9)
	print ('Hello again2! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()

tasks = [hello(), hello2(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()


