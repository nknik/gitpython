nk = lambda x: [n for n in range(2, x) if all([True if n % j != 0 else False for j in range(2, int(n ** 0.5) + 1)])]
# n=int(input())
n=15
a=nk(n)
m=[]
for i in a:
    for j in a:
        if i*j==n:
            m.extend([i,j])
if max(m)> n**(1/2):
    print("strange")
else :
    print("not strange")                

nk={}
a=[1,2,3,4,5]
nk=nk.fromkeys(a,0)
print(nk)