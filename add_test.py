#!/usr/bin/env python3

import unittest
import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.add(2, 3), 5)

    def test_error(self):
        self.assertRaises(TypeError, add.add, 1)
        self.assertRaises(TypeError, add.add, 1, 2, 3)

if __name__ == '__main__':
    unittest.main()
