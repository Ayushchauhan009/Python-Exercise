class Calculator:
    def __init__(self):
        self.x = 2
        self.y = 3

    def add(self):
        a = 10
        b = 20
        c = a + b
        return c

    def sub(self):
        a = 10
        b = 5
        d = a - b
        return d

    def multiply(self):
        a = 10
        b = 6
        y = a * b
        return y

    def division(self):
        a = 60
        b = 10
        z = a / b
        return z


c1 = Calculator()
sum = c1.add()
diff = c1.sub()
mul = c1.multiply()
div = c1.division()


print("The Sum is = ", sum)
print("The Difference is = ", diff)
print("The Multiplication is = ", mul)
print("The Division is = ", div)
