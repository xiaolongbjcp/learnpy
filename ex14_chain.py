

class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		if path =='users':
			return lambda x :Chain('/users%s/:%s' % (self._path,x))
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

url1 = Chain().usr.bin.python
url2 = Chain().users('Marx').link.tb

print (url1)
print (url2)
