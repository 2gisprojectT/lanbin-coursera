from State import State

__author__ = 'la0rg'


class StateT(State):
    def __init__(self):
        self.transitions = None

    def next(self, inp):
        if inp in self.transitions:
            action, nextState = self.transitions[inp]
            print(action)
            return nextState
        else:
            raise "Input not supported for current state"