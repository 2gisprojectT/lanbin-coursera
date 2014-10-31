__author__ = 'Uyuri'

from unittest import TestCase
import unittest
from nums import Numbers



class NumbersTest(TestCase):

    def test_init(self):
        num = Numbers(1,2,3)
        self.assertEqual(1, num.a, 'A have wrong value')
        self.assertEqual(2, num.b, 'B have wrong value')
        self.assertEqual(3, num.c, 'C have wrong value')

    def test_init1(self):
        num = Numbers(1, 2, -2)
        self.assertEqual(1, num.a, 'A have wrong value')
        self.assertEqual(2, num.b, 'B have wrong value')
        self.assertEqual(0, num.c, 'C have wrong value')

    def test_sum(self):
        num = Numbers(1, 2, -2)
        self.assertEqual(3, num.sum(), 'Sum is wrong')

    def test_multi(self):
        num = Numbers(1, -2, 2)
        self.assertEqual(-4, num.multiplication(), 'Mult is wrong')

    def test_abs_multi(self):
        num = Numbers(5,5,3)
        self.assertEqual(75.0, num.multiplication(), 'Mult is wrong')


if __name__ == '__main__':
    unittest.main()
