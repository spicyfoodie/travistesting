import unittest

class TrvTest(unittest.TestCase):
	
	def setUp(self):
		print("setup")
	
	def test_fun(self):
		print("function test")
		
if __name__=="__main__":
	unittest.main()
	

	


