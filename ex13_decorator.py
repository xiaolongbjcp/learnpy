

import functools


def log(text = ''):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if text != '':
				print (text+':')
			print ('calls %s():' % (func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


@log()
def f1():
	print ('no text!')

@log('execute')
def f2():
	print ('some text!')


f1()
f2()
