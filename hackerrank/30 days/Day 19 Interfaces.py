# xample

# The divisors of  are . Their sum is .


# The divisors of  are  and their sum is .

# Input Format

# A single line with an integer, .

# Constraints

# Output Format

# You are not responsible for printing anything to stdout. The locked template code in the editor below will call your code and print the necessary output.

# Sample Input

# 6
# Sample Output

# I implemented: AdvancedArithmetic
# 12
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = 0
        for i in range(1, n + 1):
            if n % i == 0:
                s += i
        return s


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)