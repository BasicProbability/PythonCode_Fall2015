'''
Created on Sep 21, 2015

@author: philip
'''
import unittest

# Our first unit test. We are not actually testing anything here but just illustrate how the different assert
# statements work
class SampleTest(unittest.TestCase):


    # self.assertTrue() evaluates boolean expressions. Unsurprisingly, there is also self.assertFalse()
    def test_1(self):
        self.assertTrue(1 == 1)
        
    # self.assertEqual() checks for exact equality. Notice that assertions can be supplied with optional messages.
    def test_2(self):
        self.assertEqual('Hello', 'Hello', "some message.")
        
    # This is how to use self.assertRaises in order to check whether an error has been raised correctly.
    # The part that is commented out shows you how NOT to do this.
    def test_3(self):
        my_list = list()
        # self.assertRaises(IndexError, my_list[10])
        with self.assertRaises(IndexError):
            my_list[0]


if __name__ == "__main__":
    # Conveniently, the main method for unit tests is already defined!
    unittest.main()