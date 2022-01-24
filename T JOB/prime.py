#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'checkCoPrimeExistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#
def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True


def countPrimeNumbers(numbers):
    c = 0
    for i in numbers:
        if prime(i):
            c += 1
    return c
    # return numbers

    # Write your code here


if __name__ == "__main__":
    numbers = []
    count = int(input())
    for i in range(count):
        numbers.append(int(input()))

    print(countPrimeNumbers(numbers))