a="245567"
# a=input()
nk=lambda a : int(a)+1 if int(a)%2==0 else int(a)-1
print(*list(map(nk,a)),sep="")
# 
# a="i Love to swim i Like to tavel abroad"
a=input("enter").split()
nk={}
for i in a:
    nk[i]=nk.get(i,0)+1
aa=list(nk.values())    
print(aa.count(1))

