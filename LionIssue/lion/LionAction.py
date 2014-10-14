__author__ = 'la0rg'


class LionAction:
    def __init__(self, action):
        self.action = action

    def __str__(self):
        return self.action

#Static fields:
LionAction.eat = LionAction("lion eats")
LionAction.sleep = LionAction("lion sleeps")
LionAction.run = LionAction("lion runs")
LionAction.watch = LionAction("lion watches")