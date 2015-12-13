

import unittest

from ex35_Dict import Dict 

class TestCaseForDict(unittest.TestCase):

	def test_init(self):
		d = Dict (a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key0'] = 'value0'
		self.assertEqual(d.key0, 'value0')

	def test_attr(self):
		d = Dict()
		d.key = 'value1'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value1')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

if __name__ == '__main__':
	unittest.main()
