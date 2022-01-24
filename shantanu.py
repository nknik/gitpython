a=int(input())
na=list(map(int,input().split()))
b=int(input())
nb=list(map(int,input().split()))
c=na+nb
c.sort()
print(*c[:a])
print(*c[a:])