# print(max(nk.keys()) - min(nk.keys()))
n = 558823
n = 6442
# n=int(input())
nk = lambda n: sum(list(map(int, str(n))))
aa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = nk(n)
if 0>n or n > 26:
    print("D")
else:
    print(aa[n - 1])

# =========================================
n = [2, 4, 5, 5, 4, 4]
nn = []
nk = {}
# n = int(input())
# n = int(input())
# print(n,nn)
nn=input()
n = list(map(int, input().split(',')))
for i in n:
    nk[i] = nk.get(i, 0) + 1
nik = sorted(nk.items(), key=lambda item: item[1])
print(abs(nik[0][0] - nik[-1][0]))

