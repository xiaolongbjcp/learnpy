

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print ('My name is %s.' % self.name)

s = Student('Alice')
s()
