

# http://docs.python.org/3/library/functions.html#abs

def sum(n):
	iResult = 0
	
	for i in range(n+1):
		iResult += iterm(i)

	return iResult

def iterm(i):
	return i*i + 1

print (sum(100))


