# 5
# 10
# 20
# 40
# 30
# 60
# 3
# n=[10,20,40,30,60]
n=[]
for i in range(int(input())):
    n.append(int(input()))
# k=3-1 #
k=int(input())
n.sort()
print(n)
print(n[k])
