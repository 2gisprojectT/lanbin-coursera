from unittest import TestCase
import unittest
from lion.LionInput import Input
__author__ = 'la0rg'


class LionInputTest(TestCase):

    def setUp(self):
        self.la = Input("test")

    def test_init(self):
        self.assertEquals("test", self.la.input)

    def test_str(self):
        self.assertEquals("test", self.la.__str__())

if __name__ == '__main__':
    unittest.main()