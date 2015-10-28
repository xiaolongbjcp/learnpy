

import subprocess

p = subprocess.Popen(['nslookup'], 
	stdin = subprocess.PIPE,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE
	)
output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')

print (output.decode('utf-8'))
print ('Exit codeL', p.returncode)
