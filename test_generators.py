'''
Created on Jan 12, 2019

@author: senvi
'''
import unittest
import random
from Generators_play import square_generator, random_generator


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testSquareGenerator(self):
        test_num=0;
        
        for num in square_generator(100):
            self.assertEqual(num, test_num**2, "Failed on {}".format(num))
            test_num+=1 
        
        

    def testRandomRange(self):
        test_numbers = list()
        number_of_rands=10
        start_num=20
        end_num=100
        
        for num in random_generator(number_of_rands, start_num, end_num):
            test_numbers.append(num)
            
        print(test_numbers)
        self.assertEqual(number_of_rands, len(test_numbers), "expected different number of random numbers")
        
        for num in test_numbers:
            self.assertGreater(num, start_num, "number {} is less than the lower bound of {}".format(num, start_num) )
            self.assertLessEqual(num, end_num, "number {} is greater than the upper bound of {}".format(num, end_num) )

    
    def testIterator(self):
        pass
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSquareGenerator']
    unittest.main()