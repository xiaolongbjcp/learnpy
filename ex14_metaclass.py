

class ListMetaclass(type):
	"""docstring for ListMetaclass"""
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
	pass

L = MyList()
L.add('x')
print (L)

class MyList2(list):

	def add(self, value):
		self.append(value)
	def quiry(self, value):
		return False
		

class SubMyList2(MyList2):
	"""docstring for SubMyList2"""
	def quiry(self, value):
		for el in self:
			if el == value:
				return True
		return False
		

L2 = MyList2()
L2.add('y') 
print (L2)

L3 = SubMyList2()
L3.add('z')
print (L3)
print (L3.quiry('z'))
		
