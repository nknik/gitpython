#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0 and n%5!=0:
        print("Fizz")
    elif n%3!=0 and n%5==0 :
        print("Buzz")
    else :
        print(n)
if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,n+1):
        fizzBuzz(i)
"""
Input (stdin)

Run as Custom Input
|
Download
15
Your Output (stdout)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
Expected Output

Download
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""