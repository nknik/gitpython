nk={i:i for i in range(4)}
print(nk)
nkk={i:i+1 for i in range(3,8)}
print(nkk)
n={**nkk,**nk}
print(n)
a=(1,2,34,5)
aa=(1,2,34,5)
aaa=(*a,*aa)
aaa=[a for a in aa]
print(aaa)