__author__ = 'la0rg'


class Input:
    def __init__(self, i):
        self.input = i

    def __str__(self):
        return self.input

#Stativ fields:
Input.antelope = Input("input antelope")
Input.hunter = Input("input hunter")
Input.tree = Input("input tree")