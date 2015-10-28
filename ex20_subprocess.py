

import subprocess
import os

print ('\nPid before is', os.getpid(),'\n')
r = subprocess.call(['ls'])
print ('\nPid behind is', os.getpid())



