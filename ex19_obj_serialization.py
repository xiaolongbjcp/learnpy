

import json

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score


def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

s = Student('Alice', 19, 98)

try:
	print (json.dumps(s))
except :
	print ('Error!')

sd = student2dict(s)


print ('sd:',sd)
print ('type(sd):',type(sd))
print ('json.dumps(sd):\n\t',json.dumps(sd))
print ('json.dumps(s, default = student2dict):\n\t',json.dumps(s, default = student2dict))

