# #60 891 520 213 44
# # 60 7 8 10 250 730 
# import math
# def cube(n):
#     cube_root = n**(1/3)
#     if round(cube_root) ** 3 == n:
#         return True
#     else:
#         return False
# # n=int(input())
# # nk=map(int,input().split())
# nk=[60,7,8,10,250,730]
# print(cube(sum(nk)))
# if cube(sum(nk)):
#     print("yes")
# else :
#     a=(sum(nk))**(1/3)
#     print(sum(nk))
#     print(a)
#     a=math.floor(a)+1
#     print(a)
#     new=a**3
#     print(new-sum(nk))
# ===========================================
# n=map(int,input().split())
# print(n)
# print(type(n))
# n=[0,60,7,8,10,250,730]
# def new(n):
#     if 1>n:
#         return True
# nk=filter(new,n)
# print(list(nk))

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input())
# n1, n2 = 0, 1
# count = 0
# c=0
# if nterms == 1:
#     c+=n1
# else:
#    while count < nterms:
#        c+=n1
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1
# print(c)       
# n=list(map(int,input().split()))
# nn=list(map(int,input().split()))
# nn.sort(reverse=True)
# print(nn[n[1]-1])
# def is_prime(n): 
#    if n == 1: 
#      return False 
#    for num in range(2, n//2): 
#      if n % num == 0: 
#        return False 
#    return True 
 
# nk=list(map(int,input().split()))
# nkk=[]
# for i in range(nk[0],nk[1]):
#     if is_prime(i):
#         nkk.append(i)
# sum = max(nkk) + min(nkk) 
# print("{}".format(sum))
n=list(map(int,input().split()))
nk=list(map(int,input().split()))
for i in nk:
    if i < n[1] or i > n[2]:
        print(i,end=" ")
n=int(input())
nk=list(map(int,input().split()))
k=int(input())
nk.sort(reverse=True)
for i in nk[:k]:
    print(i,end=" ")