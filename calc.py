class Calculator:
    def __init__(self):
        self.x = 2
        self.y = 3

    def add(self):
        a = 10
        b = 20
        c = a + b
        return c


c1 = Calculator()
sum = c1.add()

print("The Sum is = ", sum)
