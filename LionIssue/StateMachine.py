__author__ = 'la0rg'


class StateMachine:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()

    def runAll(self, inputs):
        for i in inputs:
            self.run(i)

    #i - instance of Input(LionInput)
    def run(self, i):
        print(i)
        nextState = self.currentState.next(i)
        if nextState is not None:
            self.currentState = nextState
        self.currentState.run()