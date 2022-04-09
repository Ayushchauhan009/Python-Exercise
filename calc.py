class Calculator:
    def __init__(self):
        self.x = 2
        self.y = 3

    def calc(self, a, b):
        c = a + b
        d = a - b
        y = a * b
        z = a / b
        return c, d, y, z


c1 = Calculator()
cal = c1.calc(8, 2)


print("The Calculations are = ", cal)
