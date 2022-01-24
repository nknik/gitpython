#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    acc = {}
    for [a, b, k] in queries:
        acc[a] = (acc[a] if a in acc else 0) + k
        acc[b + 1] = (acc[b + 1] if b + 1 in acc else 0) - k

    last = 0
    m = 0
    for i in range(1, n + 1):
        curr = acc[i] if i in acc else 0
        last = last + curr
        if last > m:
            m = last

    return m


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + "\n")

    fptr.close()
