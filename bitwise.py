# 9
# 1 7 8 5  4 6 0 2 3
# 3
n=int(input())
nk=map(int,input().split())
k=int(input())
nk=list(nk)
nk=nk[k:]+nk[0:k]
print(nk)