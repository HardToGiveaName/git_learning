#! usr/bin/env python

import unittest

class TestUnit(unittest.TestCase):
    def test_equal(self):
        i = 1
        self.assertEqual(i, 1)

    def test_true(self):
        i = 1
        self.assertTrue(isinstance(i, int))

    def test_raiseKeyError(self):
        d = {'tom':12, 'John':10}
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_raiseAttrError(self):
        d = {'tom':12, 'John':10}
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
