#!/usr/bin/env python3

"""Test module for collatz.py"""

import unittest
import pycg

class CollatzTestCase(unittest.TestCase):
    """Unit tests for collatz.py"""

    def test_eval(self):
        """collatz_eval tests"""
        self.assertEqual(pycg.collatz_eval(1, 10), 20)
        self.assertEqual(pycg.collatz_eval(100, 200), 125)
        self.assertEqual(pycg.collatz_eval(201, 210), 89)
        self.assertEqual(pycg.collatz_eval(900, 1000), 174)
        self.assertEqual(pycg.collatz_eval(1000, 900), 174)
        self.assertEqual(pycg.collatz_eval(1, 1000000), 525)
        self.assertEqual(pycg.collatz_eval(10969, 10974), 268)
        self.assertEqual(pycg.collatz_eval(837799, 837799), 525)

    def test_cycle(self):
        """collatz_cycle tests"""
        self.assertEqual(pycg.collatz_cycle(1), 1)
        self.assertEqual(pycg.collatz_cycle(2), 2)
        self.assertEqual(pycg.collatz_cycle(3), 8)
        self.assertEqual(pycg.collatz_cycle(1337), 45)
        self.assertEqual(pycg.collatz_cycle(10971), 268)
        self.assertEqual(pycg.collatz_cycle(939604), 202)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
