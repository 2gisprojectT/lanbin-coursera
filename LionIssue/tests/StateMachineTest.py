__author__ = 'la0rg'

from unittest import TestCase
import unittest
from StateMachine import StateMachine
from lion.LionMachine import Full, LionMachine, Hungry
from lion.LionInput import Input

class StateMachineTest(TestCase):

    def setUp(self):
        self.state = Full()
        self.sm = StateMachine(self.state)

    def test_init(self):
        self.assertEqual(self.state, self.sm.currentState)

    def test_run(self):
        self.sm.run(Input.antelope)
        self.assertEqual(LionMachine.hungry, self.sm.currentState)

    def test_run_1(self):
        state1 = Hungry()
        sm1 = StateMachine(state1)
        sm1.run(Input.hunter)
        self.assertEqual(state1, sm1.currentState)

    def test_run_all(self):
        self.sm.runAll([Input.antelope, Input.hunter, Input.antelope])
        self.assertEqual(LionMachine.full, self.sm.currentState)

if __name__ == '__main__':
    unittest.main()