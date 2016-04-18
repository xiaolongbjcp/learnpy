

class ListMetaclass(type):
	"""docstring for ListMetaclass"""
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(clas, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
	pass

