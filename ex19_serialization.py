

import pickle

d = dict(name='Bob', age=20, score=88)

seq = pickle.dumps(d)

print ('seq: ',seq)

f = open('test.txt', 'wb')

pickle.dump(d, f)

f.close()


f = open('test.txt', 'rb')
# seq = f.readline()
print ('seq in line:', scoreq)
d = pickle.load(f)
f.close()
print ('d in file:', d)