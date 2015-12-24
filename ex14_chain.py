

class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		if path =='users':
			return lambda x :Chain('/users/:%s/%s' % (x, self._path))
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

url1 = Chain().usr.bin.python
url2 = Chain().users('Marx').link.tb
url3 = Chain('link0').link1.users('-')

print (url1)
print (url2)
print (url3)
