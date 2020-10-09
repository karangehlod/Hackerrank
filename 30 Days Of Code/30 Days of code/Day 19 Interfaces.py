class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        count = 0
        for i in range(1, n+1):  # as n+1 is not included in range
            if n % i == 0:
                count += i
            else:
                continue
        return count


n = int(input())  # input a number to check sum of its divisors
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
