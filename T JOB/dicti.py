# ==================================================
# n=[1,2,3,4,5,6]
# a=dict()
# a=a.fromkeys(n,n)
# print(a)
# print(list(zip(n,n+n)))
# n=input()
# flag=1
# for i in n:
#     if not i.isalpha():
#         flag=0
#         break
# if flag and n==n[::-1]:
#     print("you inputted a strong string.") 
# else:
#     print("you inputted a weak string.")    
# def nk(a,b):
#     if a>1:
#         nk(a-2,b+2)
#     print(b)
 
# ==================================================
# nk(4,5)      
# n=int(input())
# c=0
# while n!=0:
#     if n%2==0:
#         n/=2
#         c+=1
#     else:
#         n-=1
#         c+=1
# print(c)
# ==================================================
n=int(input())
nk=list(map(int,input().split()))
def nik(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if (a == 0):
        m=x1/y1
        y=m*x+c
        return f"1x-1y=0"
    else:
        return 0
print(nik(*nk))
3 
# 1 1 2 2 3 3