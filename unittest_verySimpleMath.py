import unittest
from verySimpleMath import VerySimpleMath

# test class
class TestVerySimpleMath(unittest.TestCase):

	def setUp(self):
		# create object of imported class 
		self.obj = VerySimpleMath()
		
	def test_initialState(self):
		# validate initial state
		print("State nach Initialisierung: " + str(self.obj.state))
		self.assertEqual(self.obj.state, 0)
		
	def test_summation(self):
		# validate state after summation
		self.obj.increment_state()
		print("State nach Addition: " + str(self.obj.state))
		self.assertEqual(self.obj.state, 1)
		
	def test_subtraction(self):
		# validate state after subtraction
		self.obj.decrement_state()
		print("State nach Subtraktion: " + str(self.obj.state))
		self.assertEqual(self.obj.state, -1)
		
	def test_clear(self):
		# validate that state is cleared
		self.obj.clear_state()
		print("State nach Reset: " + str(self.obj.state))
		self.assertEqual(self.obj.state, 0)

if __name__ == '__main__':
	# run tests
	unittest.main()
	