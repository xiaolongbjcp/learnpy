

def foo(x, y):
	return x*10+y

L1 = [x for x in range(10,0,-1)]

L2 = reduce(foo, L1)

L3 = reduce(lambda x, y: x*10 + y, L1)

print (L2)