
nk=[-5,-3,8,-6,-7,18,10,-4,-3,11]

print(c)        
n=int(input(""))
nk=map(int,input().split())
c=0
for i in nk:
    if i <0:
        c+=1
print(c)   
# =======================================================

def cube(n):
    cube_root = n**(1/3)
    if round(cube_root) ** 3 == n:
        return True
    else:
        return False
n=int(input())
nk=map(int,input().split())
c=0
for i in nk:
    if cube(i):
        c+=1
print(c)
# =============================================================
n=39631
n=int(input())
nk=str(n)
if len(nk)%2==0:
    for i in range(0,len(nk)-1,2):
        print(nk[i],end="")
        print(nk[i+1],end="")
print(f"{nk[1]}{nk[0]}{nk[3]}{nk[2]}{nk[4]}")
# ==============================================================
a='abcdefghijklmnopqrstuvwxyz'
# n=int(input())
# for i in str(n):
#     i=int(i)
#     print(a[i],end="")
nk=input()
c=0
a='abcdefghijklmnopqrstuvwxyz1234567890'
for i in nk:
    if i not in a:
        c+=1
print(c)        
# for i in nk:
#     if not(i.isalpha()) and not(i.isdigit()):
#         c+=1
# print(c)      

# print(m.isdigit())
# print(m.isalpha())
# ==============================================================