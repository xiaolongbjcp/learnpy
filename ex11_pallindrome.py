def is_palindrome(x):
	L = list(str(x))
	l = len(L)
	for i in range(int(l/2)):
		if L[i] != L[l-1-i]:
			return False
	return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))
