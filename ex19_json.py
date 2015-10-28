

import json

d = dict(name='Bob', age=20, score=88)

j = json.dumps(d)

print ('j:', j)
print ('type of j:', type (j))
print ('d:', d)
print ('type of d:', type (d))

d2 = json.loads(j)
print ('d2:', d2)
print ('type of d2:', type (d2))