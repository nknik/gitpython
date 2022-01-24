# nk=[4,52,4,9,3,23]







nk=[]
for i in range(int(input())):
    a=int(input())
    if a not in nk:
        nk.append(a)
print(*nk,sep=' ')   
