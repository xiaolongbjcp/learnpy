

class Animal(object):
	"""docstring for Animal"""
	pass

class Mammal(object):
	pass

class Bird(object):
	pass

class Dog(Mammal):
	"""docstring for Dog"""
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(object):
	"""docstring for Ostrich"""
	pass

class Runnable(object):
	"""docstring for runnable"""
	def run(self):
		print ('Running...')

class Flyable(object):
	"""docstring for Flyable"""
	def fly(self):
		print ('Flying...')

class Hound(Dog, Runnable):
	"""docstring for hound"""
	class_name = 'Hound'

	pass

class Bat(Mammal, Flyable):
	class_name = 'Bat'
	pass

d1 = Hound()
d1.run()
print (d1.class_name)
		
		
		
		

