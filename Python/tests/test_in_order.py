#!/usr/bin/env python3

"""Test module for in_order.py"""

import unittest
import pycg

class InOrderTestCase(unittest.TestCase):
    """Unit tests for in_order.py"""

    def test_in_order(self):
        """in_order test"""
        self.assertEqual(pycg.in_order("almost"), "almost - in order")
        self.assertEqual(pycg.in_order("baton"), "baton - not in order")
        self.assertEqual(pycg.in_order("biopsy billowy chef"),
                         "biopsy - in order billowy - in order chef - not in order")

if __name__ == "__main__": # pragma: no cover
    unittest.main()
