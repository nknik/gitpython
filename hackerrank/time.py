# l = list(range(0, 10))[::-1]
# print(l)
# print(type(sorted(l)))
# l.sort()
# print(l[0])
# print(type(l))
# print(l)
# n=25
# nn=n**2
# if str(n)==str(nn)[-1*len(str(n)):]:
#     print("correct")
# else: print("wrong")
# ===============
# n = "321"
# nn = [int(n[x:y]) for x in range(len(n)+1) for y in range(len(n)+1) if x!=y and x <y ]
# print(sum(nn))
# for i in range(len(n)+1):
#     for j in range(len(n)+1):
#         if i!=j and i <j:
#             print(i,j,n[i:j])
#             nn+=int(n[i:j])
# print(nn)
# 380
# [3, 32, 321, 2, 21, 1]
# =============
# n=-6
# nn=n**4
# print(str(n),str(nn)[-1*len(str(n)):])
# if str(n)==str(nn)[-1*len(str(n)):]:
#     print("correct")
# else: print("wrong")
# ============================
# n=[1,3,5, 3, 8, 2, 6, 7, 6, 8, 9]
# nn=[]
# nn.append(n[1])
# nn.append(max(n[1:nn[-1]+nn[-1]]))
# nn.append(max(n[1:nn[-1]+nn[-1]]))
# print(nn)
# # [3, 8, 9]
# =================
# a='mama'
# b=a[-1]+a[0:-1]
# c=a[1:]+a[0]
# print(b,c)
# print(True if c==b else False)
# ==================
# n = [12, 22, 33, 45, 67, 333, 314, 5432]
# nk = lambda n: sorted(list(set(str(n)))) == sorted(list(str(n)))
# # print(list(set(str(n[-1]))).sort() , list(str(n[-1])).sort())
# #
# # for i in n: print(i,nk(i))
# a = list(filter(nk, n))
# print(a)
# # print([1,2,3]==[1,2,3])
# ===================================
# n=list(range(4,30))
# isprime=lambda a : all((a%i)!=0 for i in range(2,int(a**.5)+1))
# nn=list(filter(isprime,n))
# for i in nn:
#     for j in nn:
#         if i-j==6 :
#             print(i,j)
#  ==============================
import re
n='This is alpha 55 5057 and 97'
# n='dream job 100 and 101'
# for i in n.split():
#     if i.isdigit()  and str(9) not in i :
#         print(i)
print(re.findall('\d+',n))        
# a=re.match('55',n)    
# 
import re

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
# print(dir(x))
          
# print(type(a),a)
print(re.search('\d+',n).span()) 
# for i in re.search('\d+',n) : print(i)    
n=[1,2,3]
print(n[:6])