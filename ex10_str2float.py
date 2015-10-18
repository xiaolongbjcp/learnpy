

from functools import reduce

def str2float(s):
	intp = list(s.split('.')[0])
	parp = list(s.split('.')[1])
	l = len(parp)
	intp = reduce(intf, intp)
	parp = reduce(intf, parp)*1.0/pow(10, l)
	return intp + parp

def intf(x, y):
	return (int(x)*10 + int(y))	

print('str2float(\'123.456\') =', str2float('123.456'))
