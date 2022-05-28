# Python program to print prime factors and distinct prime factors
import math


def primeFactors(n):
    nk = []
    while n % 2 == 0:
        nk.append(2),
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            nk.append(i),
            n = n / i
    if n > 2:
        nk.append(n)
    return len(set(nk))


n = int(input())
n = list(map(int, input().split()))
k = int(input())
aa = list(map(primeFactors, n))
# custom input
# k = 2
# n = [16, 38, 26, 12, 26]
print(aa.count(k))
# print(n,k)


















