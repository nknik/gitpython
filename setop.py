#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'setOperation' function below.
#
# The function is expected to return a union, intersection, difference(a,b), difference(b,a), symmetricdifference and frozen set.
# The function accepts following parameters:
#  1. List seta
#  2. List setb
#


def setOperation(seta, setb):
    # Write your code here
    pass
    seta = set(seta)
    setb = set(setb)
    a = seta.union(setb)
    b = seta.intersection(setb)
    c = seta.difference(setb)
    d = setb.difference(seta)
    e = seta.symmetric_difference(setb)
    f = frozenset(seta)
    return a, b, c, d, e, f


if __name__ == "__main__":
    seta_count = int(input().strip())

    seta = []

    for _ in range(seta_count):
        seta_item = input()
        seta.append(seta_item)

    setb_count = int(input().strip())

    setb = []

    for _ in range(setb_count):
        setb_item = input()
        setb.append(setb_item)

    un, intersec, diffa, diffb, sydiff, frset = setOperation(seta, setb)
    print(sorted(un))
    print(sorted(intersec))
    print(sorted(diffa))
    print(sorted(diffb))
    print(sorted(sydiff))
    print(
        "Returned value is {1} frozenset".format(
            frset, "a" if type(frset) == frozenset else "not a"
        )
    )
