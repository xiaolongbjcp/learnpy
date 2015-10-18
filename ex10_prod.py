

from functools import reduce

def prodf(x, y):
	return x*y

def prod(L):
	return reduce(prodf, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))