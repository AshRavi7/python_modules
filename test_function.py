# Python testing-Python has a built in module 'unitest' , from the name itself it is used to test unit components of code whereas integration testimg is used to test multiple components of the code. 

# unit test comes with different methods to assert on the values,types and variables. 

# .assertEqual(condition,result)
# .assertTrue(condition)
# .assertFalse(condition)
# .assertIs(a.b) # test whether a is b 
# .assertIsNone(x) # test whether x is None
# .assertIsInstance(a,b)

from function import add,product # from root_directory.file_name/sub_directory import function_name/class_name
import unittest 

class test_function(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,20),30)
        self.assertNotEqual(add(10,20),40)
        self.assertIs(10,10)
        self.assertIsInstance("1",str)
        self.assertIn(10,[12,13,10,18])
    def test_product(self):
        self.assertEqual(product(10,10),100)
        self.assertNotEqual(product(10,20),40)
if __name__=='__main__':
    unittest.main()
        
        
    