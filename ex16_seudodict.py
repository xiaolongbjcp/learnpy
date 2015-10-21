

class Dict(dict):
	"""docstring for Dict"""
	def __init__(self, **kw):
		super().__init__(**kw)

	def __setattr__(self, key, value):
		self[key] = value

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("'Dict' object has no attribute '%s'" % key)

d = Dict(a=1, b=2)
print (d['a'])
print (d.a)
d.a = 3
print (d.a)
d['a'] = 4
print (d['a'])
print (d.c)

