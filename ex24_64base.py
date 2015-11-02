

import base64


def safe_base64_decode(s):
	slen = len(s) % 4
	# if slen == 0:
	# 	return base64.b64decode(s)
	# else:
	# 	s0 = s + b'='*(4 - slen)
	# 	return base64.b64decode(s0)

	s0 = s + b'='*(4 - slen)
	return base64.b64decode(s0)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
