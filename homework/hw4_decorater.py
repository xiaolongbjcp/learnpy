
def log(x):
	def wrapper(func):
		def inner(*args, **kw):
			print ('log:')
			return func(*args, **kw)
		return inner
	return wrapper



@log('!')
def f1(x):
	print ('Hello,', x)

f1('jack')


# return func(*args, **kw)

# print ('log')
# return func(*args, **kw)

# def inner(*args, **kw):
# 	print ('log')
# 	return func(*args, **kw)
	
# def outter(func):
# 	def inner(*args, **kw):
# 		print ('log')
# 		return func(*args, **kw)
#	retrun inner

	
def outter(func):
	def inner(*args, **kw):
		print ('log')
		return func(*args, **kw)
	return inner

@outter
def f2(i):
	print ('you are',i)

f2('xiaolong')



