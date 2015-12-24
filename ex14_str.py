

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		print (self.name)
		return 'this is "%s"' % self.name

	__repr__ = __str__


	
print (Student('S1'))
s = Student('S2')
print (repr(s))