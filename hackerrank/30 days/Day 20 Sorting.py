# #sorting
# Day 20: Sorting

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
s=0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j],a[j + 1]=a[j+1],a[j]
            s += 1
    if s == 0:
        break

print("Array is sorted in " + str(s) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a) - 1]))