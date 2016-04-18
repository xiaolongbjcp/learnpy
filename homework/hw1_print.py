#-*- oding: utf-8 -*-

# name = input('hi, what\'s your name?\n\t')
# print ( 'hello, %s!' % (name))

print ( '1024 * 768 =',  1024 * 768)

print ( '0x18:', (0x18))

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

l_hw1 = [n, f, s1, s2, s3, s4]

print (l_hw1)

for i in l_hw1:
	print (type(n))
	print (i)

print (12e-5)
print (1.2e-4)

str1 = 'qwerty'
try:
	str1[2] = 'a'
	print ('str1 = ', str1)
except:
	print ("str1[2] = 'a' --- Operation failed!")
	print ('str1[2] = ', str1[2])

print ([str(x*(x+1))+y for x in range(4) for y in ['a','b', 'c', 'd']])
# print ([str(x*(x+1)) for x in range(4)])
print ('0x%x' % (18))

s1 = 72
s2 = 85
r = (s2-s1)/s2
print ('%.1f%%'%r)

classmate = ('A', 'B', 'C', 'D', ['E', 'F'], (1,), (2, 3))
print ( classmate[0], classmate[4][-1], classmate[4][0], classmate[5][0], classmate[6][1])
print ( type(classmate), ':', classmate )

height = 1.75
weight = 80.5
bmi = weight / height**2
# print (bmi)
if bmi <= 18.5:
	print ('light!')
elif 18.5 <= bmi and bmi < 25:
	print ('normal!')
elif 25 <= bmi and bmi < 28:
	print ('weight!')
elif 28 <= bmi and bmi < 32:
	print ('so weight!')
elif 32 <=bmi:
	print ('extramely weight!')

for i in classmate:
	print ('Hello,', i)

n1 = 255
n2 =1000
print ('hex of \'255\' is', hex(255))


import math

def quadratic (a, b, c):
	delta = b**2 - 4*a*c
	if delta < 0:
		return (None, None)

	r1 = (-b + math.sqrt(delta))/(2*a)
	r2 = (-b - math.sqrt(delta))/(2*a)
	return (r1, r2)

print (quadratic (1, 2, 1))

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1, 2, 'a', 'b', x=11)

def move(n, a, b, c):
	if n==1:
		print (a, '-->', c)
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n-1, b, a, c)

move(3, 'A', 'B', 'C')

r = range(100)
print (type(r), ':', r)
l = list (r)
print (l)

print (l[:0])
print (l[:1])
print (l[1:])
