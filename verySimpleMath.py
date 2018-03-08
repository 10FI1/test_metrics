class VerySimpleMath(object): 
	def __init__(self): 
		self.state = 0
 
	def increment_state(self): 
		#if self.state == 0:
		#	self.state += 10
		#elif self.state == 3:
		#	if self.state < 2:
		#		self.state += 5
		#	elif self.state == 1: 
		#		self.state += 100
		#	elif self.state > 1:
		#		self.state += 3
		#	else:
		#		self.state += 50
		#else: 
		self.state += 1

	def decrement_state(self):
		self.state -= 1
		
	def clear_state(self): 
		self.state = 0