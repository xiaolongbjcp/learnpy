

def fib(max):
	n = 0
	a = 0
	b = 1
	while n < max:
		print (b)
		# temp = b		
		# b = a + b
		# a = temp
		a, b = b, a + b
		n += 1
	return 'the end'


def fib_gen(max):
	n = 0
	a = 0
	b = 1
	while n < max:
		yield b
		a, b = b, a + b
		n += 1
	# return 'the end'

f = fib (20)

g = fib_gen (20)

for i in g:
	print (i)
