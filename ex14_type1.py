

def foo(self, name = 'world'):
	print ('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello = foo))

h = Hello()
h.hello()