

# the item using must be the one never edited before

def triangles(max):
	n = 1
	L = [1]
	while True:
		print L
		n += 1
		
		if n == 1:
			L = [1]
		elif n == 2:
			L = [1, 1]
		elif n > 2:
			length = len (L)
			for i in range(1, length):
				L[length - i] = L[length - i] + L[length - i -1]
			L.append(1)

		if n > max:
			break

triangles(5)

def triangles_gen():
	n = 1
	L = [1]
	while True:
		yield L
		n += 1
		
		if n == 1:
			L = [1]
		elif n == 2:
			L = [1, 1]
		elif n > 2:
			length = len (L)
			for i in range(1, length):
				L[length - i] = L[length - i] + L[length - i -1]
			L.append(1)

		# if n > max:
		# 	break


# t = triangles_gen()
n = 0
for t in triangles_gen():
    print(t)
    n = n + 1
    if n == 10:
        break