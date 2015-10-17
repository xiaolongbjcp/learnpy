


import math

def quadratic (a, b, c):
	
	delta = b**2 - 4*a*c

	if delta < 0:
		print ('No root exist!')
		return None
	elif delta == 0:
		print ('1 root exists!')
		root = (-b) / (2*a)
		return root
	else:
		print ('2 root exist!')
		root1 = (-b + math.sqrt(delta) ) / (2*a)
		root2 = (-b - math.sqrt(delta) ) / (2*a)
		return (root1, root2)

print (quadratic(1, 1, 1))
print (quadratic(1, -2, 1))
print (quadratic(2, 3, 1))
print (quadratic(1, 3, -4))