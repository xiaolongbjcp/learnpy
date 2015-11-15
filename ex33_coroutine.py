

def consumer():
	r = ''
	print ('.....')
	while True:
		print (0)
		n = yield r
		print(1)
		print (str(n)+'..\n')
		if not n:
			print ('Initialized!\n')
			# return '000'
		print ('[Consumer] Consuming %s...' % n)
		r = '200 OK'

def produce(c):
	r = c.send(999)
	print ('send None to consumer...', r)
	n = 0
	while n < 2:
		n = n + 1
		print ('{Producer} Producing %s...' % n)
		r = c.send(n)
		print ('{Producer} Consumer return %s\n' % r)
		# n = n + 1
	c.close()

con = consumer()
produce(con)