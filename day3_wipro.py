# def cube(n):
#     cube_root = n**(1/3)
#     if round(cube_root) ** 3 == n:
#         return True
#     else:
#         return False
# n=raw_input()
# nk=list(map(int,raw_input().split()))
# c=0
# for i in nk:
#     if cube(i):
#         c+=1
# print c

# nk=['3521','2452','1352']
# a=nk[0][0]+nk[1][0]+nk[2][0]
# b=nk[0][1]+nk[1][1]+nk[2][1]
# c=nk[0][2]+nk[1][2]+nk[2][2]
# d=nk[0][3]+nk[1][3]+nk[2][3]
# print(min(a)+max(b)+min(c)+max(d))
# n=raw_input()
# nk=list(map(int,raw_input().split()))
nk = [2, 4, 5, 5, 4]
nk = [2, 3, 4, 3, 4, 4]
nk = [2, 3, 2, 3, 5, 5, 5]

# n=raw_input()
# nk=list(map(int,raw_input().split()))
big = 0
b = 0
small = 10
s = 0
n = 6
k = {x: nk.count(x) for x in nk}
for i, j in k.items():
    if big < j:
        big = j
        b = i
    if small > j:
        small = j
        s = i
print(abs(b - s))
