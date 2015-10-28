




import os

print ('Process id is:', os.getpid())

print ('the parent pid at th first time after fork(), and child behind:')
os.fork()
print ('this line will emerge 2 times.')
print ('Process id:', os.getpid())


