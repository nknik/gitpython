#!/bin/python3
# print in reverse
import math
import os
import random
import re
import sys


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for i in arr[::-1]:
        print(i, end=" ")