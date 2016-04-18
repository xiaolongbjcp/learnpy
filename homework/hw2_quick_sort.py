
def quick_sort(l, left, right):

	print ('l=', l[left: right+1])
	h = left
	m = left
	t = right


	if h >= t:		
		print ('l =', l, '\n')
		return l
	

	while (h < t):
		if l[h] <= l[m]:
			h += 1
		else:
			if l[m] <= l[t]:
				t -= 1
			else:
				temp = l[h]
				l[h] = l[t]
				l[t] = temp
				if l[m] > l[t]:
					print ('!!')
					break
	if l[m] > l[h]:
		temp = l[m]
		l[m] = l[h]
		l[h] = temp


	quick_sort(l, left, h-1)
	
	quick_sort(l, h, right)


	return l
	

l = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
l1 = [1]
l2 = [2, 1]

print ('result:', quick_sort(l, 0, 9))

# l3 = [x for x in range(100, 0, -1)]
# print (l3)
# print ('result:', quick_sort(l3, 88, 99))


