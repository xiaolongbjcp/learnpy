

def fact(n):
	return fact_iter(n,1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

def fact2(n, temp = 1):
	if n == 1:
		return temp
	return fact2(n-1, n * temp)

print (fact(5))
print (fact2(5))

