__author__ = 'la0rg'


class LionAction:
    def __init__(self, action):
        self.action = action

    def __str__(self):
        return self.action

#Static fields:
LionAction.eat = LionAction("lion_test eats")
LionAction.sleep = LionAction("lion_test sleeps")
LionAction.run = LionAction("lion_test runs")
LionAction.watch = LionAction("lion_test watches")