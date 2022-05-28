l=[50,60,70,80,90,10]
def x(a,b):l[a],l[b]=l[b],l[a]
[x(a,b) if l[a]>l[b] else 0 for a in range(len(l)) for b in range(a,len(l))]
print(l)