import unittest
from basic import BasicFunction

class TestBasicFunction(unittest.TestCase):

	def setUp(self):
		self.func = BasicFunction()
		
	def test_drei(self):
		self.assertEqual(self.func.state, 0)
	def test_vier(self):
		self.func.increment_state()
		self.assertEqual(self.func.state, 1)
	def test_fuenf(self):
		self.func.increment_state()
		self.func.increment_state()
		self.func.clear_state()
		self.assertEqual(self.func.state, 0)
		

if __name__ == '__main__':
	unittest.main()