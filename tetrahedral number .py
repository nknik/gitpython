#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateNTetrahedralNumber' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#


def calculateNTetrahedralNumber(startvalue, endvalue):
    # Write your code here
    return [(n * (n + 1) * (n + 2)) // 6 for n in range(startvalue, endvalue + 1)]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    startvalue = int(input().strip())

    endvalue = int(input().strip())

    result = calculateNTetrahedralNumber(startvalue, endvalue)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
