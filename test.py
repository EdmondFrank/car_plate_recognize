# -*- coding: utf-8 -*-

import unittest
from train import *

class TestTrain(unittest.TestCase):
    def setUp(self):
        #print("do something before test.Prepare environment.")
        pass
    def tearDown(self):
        pass
        #print("do something after test.Clean up.")
    def test_vec2text(self):
        """Test method add(a, b)"""
        print("test_vec2text")
        test = text2vec("云F71K64")
        self.assertEqual("云F71K64", vec2text(test))
    def test_text2vec(self):
        print("test_text2vec")
        vec = text2vec("云F71K64")
        self.assertEqual(1, vec[43+68*0])
        self.assertEqual(1, vec[15+68*1])
        self.assertEqual(1, vec[7+68*2])
        self.assertEqual(1, vec[1+68*3])
        self.assertEqual(1, vec[20+68*4])
        self.assertEqual(1, vec[6+68*5])
        self.assertEqual(1, vec[4+68*6])
        #print(vec)

if __name__ == '__main__':
    unittest.main()