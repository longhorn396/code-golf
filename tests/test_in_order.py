#!/usr/bin/env python3

"""Test module for in_order.py"""

import unittest
from in_order import in_order

class InOrderTestCase(unittest.TestCase):
    """Unit tests for in_order.py"""

    def test_in_order(self):
        """in_order test"""
        self.assertEqual(in_order("almost"), "almost - in order")
        self.assertEqual(in_order("baton"), "baton - not in order")
        self.assertEqual(in_order("biopsy billowy chef"),
                         "biopsy - in order billowy - in order chef - not in order")
