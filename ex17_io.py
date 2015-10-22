

f = open('./test.txt', 'w')
f.write('This line is for testing I/O.\n')
f.close()

with open('./test.txt', 'a') as f:
	f.write('This line is add to the file.\n')
	f.close()
	f = open('./test.txt', 'rb')
	lines = f.read()
	print (lines)
	f.close()