import math

class Numbers(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        if c > 0:
            self.c = c
        else:
            self.c = 0

    def sum(self):
        return self.a + self.b + self.c

    def multiplication(self):
        return self.a * self.b * self.c

    def abs_multiplication(self):
        return math.fabs(self.a * self.b * self.c)