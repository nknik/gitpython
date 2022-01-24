# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17
# print nth number
def fib(n):
    nk = [1, 1]
    for i in range(n):
        nk.append(nk[-1] + nk[-2])
    return nk


nk = lambda x: [
    n
    for n in range(2, x)
    if all([True if n % j != 0 else False for j in range(2, int(n ** 0.5) + 1)])
]
print(nk(30))
print(fib(5))
n = 177
a = []
for x, y in zip(fib(n), nk(n)):
    a.extend([x, y])
print(a[14 - 1])


n = list(map(int, input().split()))
nn = list(map(int, input().split()))
nk = []
for i in nn:
    nk.append(n[i])
print(max(nk))