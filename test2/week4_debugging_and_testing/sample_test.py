'''
Created on Sep 21, 2015

@author: philip
'''
import unittest


class SampleTest(unittest.TestCase):


    def test_1(self):
        self.assertTrue(1 == 1)
        
    def test_2(self):
        self.assertEqual('Hello', 'Hello', "some message.")
        
    def test_3(self):
        my_list = list()
        # self.assertRaises(IndexError, my_list[10])
        with self.assertRaises(IndexError):
            my_list[0]


if __name__ == "__main__":
    unittest.main()