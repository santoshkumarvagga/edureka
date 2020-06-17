import unittest


class Hey(unittest.TestCase):
	a = 40
	b = 5

	@classmethod
	def setUpClass(cls):
		print("Entered into Class")

	def setUp(self):
		print("Starting Testing of a function")

	def sum(self):
		return self.a + self.b

	def test_validate(self):
		'''Testcase to test sum() function'''
		assert self.sum() == 45, 'sum failed'

	def tearDown(self):
		print("Finsihed Testing")

	@classmethod
	def tearDownClass(cls):
		print("Leaving the class")


Hey()


if __name__ == '__main__':
	unittest.main()
