

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1 

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration();
		return float(self.a/self.b)

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1,1
			for x in range(n):
				a, b = b, a+b
			return a

		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			if stop is None:
				stop = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b =	 b, a + b

			return L


for n in Fib():
	print (n)

f = Fib()
for i in range(10):
	print (f[i])
	
print (f[:10])
print (f[8:])
print (f[1:4])