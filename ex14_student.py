

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
Alice.name = 'alice'
Alice.address = 'Beijing'
print (Alice.name)
print (Alice.address)
print ('Alice._Student__score is accessable:', Alice._Student__score)
# err
# print ('score is rejected:', Alice.__score)

Alice.__score = 100
Alice.print_score()

# bug??
print ('score changed is accessable:', Alice.__score)
		
