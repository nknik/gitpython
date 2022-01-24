# # n = 6  # int(input())
# # print(sum([x for x in range(1, n + 1) if n % x == 0]))
# # n = int(input())
# # nk = input().split()
# # n = int(input())
# # if nk == "":
# #     print("NULL")
# # else:
# #     for i in range(n):
# #         a = nk.pop(0)
# #         nk = nk + [a]
# #     # print(" ".join(nk))
# #     print(*nk, sep=" ")
# y=1
# for i in range(0,5):
#     for j in range(0,i+1):
#         y=y**(j+1)
# print(y)  
# def nkk(n):
#     print(n)      
# def nk(y):
#     if y==1:
#         return 1
#     if y==2:
#         return 2
#     y=3
#     return nkk(5),nkk(y-2)
# print(nk(3))    
# class nk(object):
#     def __init__(self) -> None:
#         super().__init__()
#     @classmethod
#     def krishna(cls):
#         pass    
#     def __add__(self):
#         pass    
#     @staticmethod
#     def itisstat():
#         pass    
#         print("this is static")
nk="krishna"
print(nk[9::-1])
a=["aba",'aaa',"acd"]
aa=lambda a:a[::-1]==a
def chck(a):
    return a[::-1]==a
print(list(filter(aa,a)))
n=2
# n=int(input())
nk=[0,1]
nk[0]=0
nk[1]=1
c=2
while len(nk)!=n:
    pass
    nk.append(nk[c-1]+2*nk[c-2]+3)
    c+=1
print(nk[n-1])    