
def f(x):
	return x**2

r = map( f, [x for x in range(10)])
print (list(r))

def normalize(str):
	return str.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod (L):
	def f(x, y):
		return x*y

	return reduce(f, L)

print ('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def is_palindrome(n):
	l = str(n)

	lt = len(l)
	i=0
	j=lt-1

	while (i < j):
		if l[i] != l[j]:
			return False
		else:
			i += 1
			j -= 1

	return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))
