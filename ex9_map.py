

def foo(i):
	return i**2

L1 = [x for x in range(10)]

L2 = map (foo, L1)

print (L2)

