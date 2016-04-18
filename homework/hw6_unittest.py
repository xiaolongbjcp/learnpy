
import unittest
import hw5_sudoDict

class TestCaseForSudoDict(unittest.TestCase):
	"""docstring for TestCaseForSudoDict"""
	# def __init__(self, arg):
	# 	super(TestCaseForSudoDict, self).__init__()
	# 	self.arg = arg

	def setUp(self):
		print ('Begining!')
		self.d = hw5_sudoDict.Dict()
	
	def test_init(self):
		d1 = hw5_sudoDict.Dict(a=1, b='test_init')
		self.assertTrue(isinstance(d1, dict))
		self.assertEqual(d1.a, 1)
		self.assertEqual(d1.b, 'test_init')

	def test_keyerror(self):
		with self.assertRaises(KeyError):
			print (self.d['a'])

		with self.assertRaises(AttributeError):
			print (self.d.a)

	def tearDown(self):
		print ('Finished!')




if __name__ == '__main__':
	unittest.main()
