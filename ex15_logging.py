

import logging

logging.basicConfig(level=logging.INFO)

def foo(s):
	return 10/int(s)

def bar(s):
	logging.info('in bar: s = %s' % s)
	return foo(s)*s

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('the end')
