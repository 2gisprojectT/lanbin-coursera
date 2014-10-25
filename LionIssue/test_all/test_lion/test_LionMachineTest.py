from unittest import TestCase
import unittest
from lion.LionInput import Input
from lion.LionMachine import LionMachine, Full, Hungry

__author__ = 'la0rg'


class LionMachineTest(TestCase):

    def test_init(self):
        lm = LionMachine()
        self.assertEqual(LionMachine.full, lm.currentState)


class FullTest(TestCase):

    def test_next(self):
        full = Full()
        self.assertEqual(LionMachine.hungry, full.next(Input.hunter))
        self.assertRaises(Exception, full.next, 1)


class HungryTest(TestCase):

    def test_next(self):
        hungry = Hungry()
        self.assertEqual(None, hungry.next(Input.hunter))
        self.assertRaises(Exception, hungry.next, 1)

if __name__ == '__main__':
    unittest.main()