

def normalize(name):
	name = list (name.lower())
	name[0] = name[0].upper()
	return ''.join(name)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
