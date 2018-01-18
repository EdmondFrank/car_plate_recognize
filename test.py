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

if __name__ == '__main__':
    unittest.main()