

def get_new_port():
	n = 8888
	while n > 1024:
		yield n		
		n -= 1

print (get_new_port())
print (get_new_port())
print (get_new_port())

x = get_new_port()
print (next(x))
print (next(x))
print (next(x))