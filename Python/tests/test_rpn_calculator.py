#!/usr/bin/env python3

"""Test module for rpn_calculator.py"""

import unittest
import pycg

class RPNCalculatorTestCase(unittest.TestCase):
    """Unit tests for rpn_calculator.py"""

    def help_test(self, stack, result):
        """Helper for tests"""
        self.assertEqual(pycg.iterative_rpn(stack), result)
        self.assertEqual(pycg.recursive_rpn_wrap(stack), result)

    def test_rpn_calculator_simple(self):
        """Simple test for the rpn_calculator algos"""
        self.help_test("2 3 +", 5)

    def test_rpn_calculator_complex(self):
        """Complex test for the rpn_calculator algos"""
        self.help_test("2 3 + 3 * 1 - 7 / 2 %", 0)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
