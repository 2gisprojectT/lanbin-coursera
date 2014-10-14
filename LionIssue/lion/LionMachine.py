from lion.LionAction import LionAction
from StateMachine import StateMachine
from StateT import StateT
from lion.LionInput import Input

__author__ = 'la0rg'


class Full(StateT):
    def run(self):
        print("Lion's full!")

    def next(self, inp):
        # Lazy init
        if not self.transitions:
            self.transitions = {
                Input.antelope: (LionAction.sleep, LionMachine.hungry),
                Input.hunter: (LionAction.run, LionMachine.hungry),
                Input.tree: (LionAction.watch, LionMachine.hungry)
            }
        return StateT.next(self, inp)


class Hungry(StateT):
    def run(self):
        print("Lion's hungry!")

    def next(self, inp):
        # Lazy init
        if not self.transitions:
            self.transitions = {
                Input.antelope: (LionAction.eat, LionMachine.full),
                Input.hunter: (LionAction.run, None),
                Input.tree: (LionAction.sleep, None)
            }
        return StateT.next(self, inp)


class LionMachine(StateMachine):
    def __init__(self):
        #Initial state
        StateMachine.__init__(self, LionMachine.full)

# Static variables:
LionMachine.full = Full()
LionMachine.hungry = Hungry()

lionMachine = LionMachine()
lionMachine.run(Input.antelope)
lionMachine.run(Input.hunter)
lionMachine.run(Input.tree)
lionMachine.run(Input.antelope)
lionMachine.run(Input.tree)
