

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.__score = score

	def print_score(self):
		print ('%s:%s' % (self.name, self.__score))

	def set_score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer!')
		if (score<0 or score > 100):
			raise ValueError('score must between 0 ~ 100!')
		self.__score = score

	# def score(self, tuple):
	# 	value = tuple[0]
	# 	offset = tuple[1]
	# 	if not isinstance(value, int):
	# 		raise ValueError('score must be an integer!')
	# 	if value < 0 or value > 100:
	# 		raise ValueError('score must between 0 ~ 100!')
	# 	self._score = value + offset


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





def set_age(self, age):
	self.age = age

s = Student('s', 100)
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(16)
print ('the age of student s is',s.age)

s.set_score(60)
print (getattr(s, 'name'))
print (getattr(s, '_Student__score'))
s.print_score()
print ('s.name is', s.name)


class Student2(object):

	@property
	def score(self):
		print ('here!')
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value


s2 = Student2()
s2.score = 61
print (s2.score)

