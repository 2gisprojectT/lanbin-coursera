from unittest import TestCase
import unittest
from lion.LionAction import LionAction

__author__ = 'la0rg'


class LionActionTest(TestCase):

    def setUp(self):
        self.la = LionAction("test")

    def test_init(self):
        self.assertEquals("test", self.la.action)

    def test_str(self):
        self.assertEquals("test", self.la.__str__())

if __name__ == '__main__':
    unittest.main()