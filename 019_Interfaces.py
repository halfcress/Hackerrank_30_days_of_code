class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def __init__(self):
        self.n = n

    def divisorSum(self, n):
        l = []
        for i in range(1, self.n + 1):
            if self.n % i == 0:
                l.append(i)
        return sum(l)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)