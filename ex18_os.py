

import os

# def dir_l():
# 	dirlist = [d for d in os.listdir('.') if os.path.isdir(d)]
# 	print (dirlist)

# 	fillist = [f for f in os.listdir('.') if os.path.isfile(f)]
# 	print (fillist)


# dir_l()

# def dir_list():
# 	return [d for d in os.listdir('.') if os.path.isdir(d)]

# def file_list():
# 	return [f for f in os.listdir('.') if os.path.isfile(f)]
	
# def search(file_name):
# 	return file_name in file_list()

# target1 = 'ex1_sum.py'
# print (search(target1))

# def dir_list2(inpath):
# 	# return [d for d in os.listdir(inpath) if os.path.isdir(inpath + '/' + d)]
# 	return [d for d in os.listdir(inpath) if os.path.isdir(os.path.join(inpath, d))]

# def fil_list2(inpath):
# 	# return [f for f in os.listdir(inpath) if os.path.isfile(inpath + '/' + f)]
# 	return [f for f in os.listdir(inpath) if os.path.isfile(os.path.join(inpath, f))]

# def search2(file_name, inpath):
# 	return file_name in fil_list2(inpath)


# target2 = 'ex1_sum.py'
# print (search2(target2, '.'))
# print (dir_list2('.'))

# target2 = 'test1.txt'
# inpath = './test'
# print (search2(target2, './test'))
# print (dir_list2('./test'))


# def dir_list3(inpath):
# 	return [os.path.join(inpath, d) for d in os.listdir(inpath) if os.path.isdir(os.path.join(inpath, d))]

# def file_list3(inpath):
# 	return [os.path.join(inpath, f) for f in os.listdir(inpath) if os.path.isfile(os.path.join(inpath, f))]

# def search3(file_name, inpath):
# 	return os.path.join(inpath, file_name) in file_list3(inpath)

# target3 = 'test1.txt'
# inpath = './test'
# print (search3(target3, './test'))
# print (dir_list3('./test'))

def dir_list4(inpath):
	return [os.path.join(inpath, d) for d in os.listdir(inpath) if os.path.isdir(os.path.join(inpath, d))]

def file_list4(inpath):
	return [os.path.join(inpath, f) for f in os.listdir(inpath) if os.path.isfile(os.path.join(inpath, f))]

def search4(file_name, inpath):
	# return os.path.join(inpath, file_name) in file_list4(inpath)
	print ('----------------------------------------')
	# tempfile = os.path.join(inpath, file_name)
	# tempdirlist = file_list4(inpath)
	# print ('file      :  ', tempfile,':',type(tempfile) )
	# print ('file_list4:', tempdirlist[0],':',type(tempdirlist[0]))
	# print ('assert:', tempfile in tempdirlist)
	# print ('ass2: ', os.path.isfile(tempfile))
	if os.path.join(inpath, file_name) in file_list4(inpath):
	# if tempfile in tempdirlist:
		print ('Here!!!!!!!!!!!!!!!!', inpath)
		return inpath
	else:
		for sub_dir in dir_list4(inpath):
			# in2path = os.path.join(inpath, sub_dir)
			if sub_dir == './.git':
				pass
			else:
				in2path = sub_dir
				# file_name = os.path.join(in2path, file_name)
				print ('in2path: ', in2path)
				print ('file_name: ', file_name)
				if search4(file_name, in2path):
					return in2path


target4 = 'test1.txt'
inpath = '.'
print (search4(target4, inpath))
print (dir_list4('./test'))


