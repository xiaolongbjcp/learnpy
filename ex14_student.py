

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.__score = score

	def print_score(self):
		print ('%s:%s' % (self.name, self.__score))

Alice = Student('Alice', 99)
Bob = Student('Bob', 98)

print ("Student's name:", Alice.name)
Alice.print_score()
# print ('score is rejected:', Alice.__score)
		
