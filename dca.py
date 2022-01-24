# n=int(input())
# k=int(input())
nk = lambda a: len(set(str(a))) == len(str(a))
a = 101010
print(nk(str(a)))
print(len(list(filter(nk, range(101, 200)))))
# =======================================
nk = list(map(int, "10 20 30 40".split()))


def nik(a, k):
    aa = a.pop(0)
    print(a,aa)
    while k:
        a = [a[-1]] + a[0:-1]
        k-=1
    a.insert(0, aa)
    return a


print(nik(nk, 1))
# =======================================

nk = list(map(int, "100 21 5 6 3 7 11 89 10".split()))
n=[]
k=[]
for i in nk:
    if i%10==0:
        k.append(i)
    else:
        n.append(i)
print(*n,*k,sep=" ")            
nk = list(map(int, "10, 20, 30, 40, 50".split(',')))
k=2
print(*nk[k:],*nk[:k],sep=" ")
print(int(1.90))
# =======================================
# nk = list(map(int, "10, 20, 30, 40, 50".split(',')))
def nik(r,n,rr,x):
    pass
    import math as m
    x=m.ceil(x/60)
    cost=0
    if x<= n:
        return r*x
    elif x > n:
        cost+=r*n
        cost+=rr*(x-n)
        return cost


print(nik(20,4,40,300))
print(nik(30,5,35,500))
print(nik(30,10,35,5))