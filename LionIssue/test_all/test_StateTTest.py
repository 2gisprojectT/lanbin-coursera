from unittest import TestCase
import unittest
from StateT import StateT

__author__ = 'la0rg'


class StateTTest(TestCase):

    def setUp(self):
        self.st = StateT()

    def test_init(self):
        self.assertEquals(None, self.st.transitions)

    def test_next_empty(self):
        self.assertRaises(Exception, self.st.next, 1)

    def test_next(self):
        self.st.transitions = {
            1: ("action", "next_state")
        }
        self.assertEquals("next_state", self.st.next(1))

if __name__ == '__main__':
    unittest.main()
