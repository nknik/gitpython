lst=list()
tup=tuple()
st=set()
dt=dict()
str=''
nk=['list@']+[i for i in dir(lst)]+['str@']+[i for i in dir(str)]
# print(dir(a))
print([print(i) for i in nk ])
# print(dir(x))
# print(dir(y))
# print(dir(z))