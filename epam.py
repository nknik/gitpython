def chck(n):
    n.sort()
    c=0
    while(max(n)>n[0] and min(n)>0):
        n[0]=n[0]+n[1]
        c+=1    
    return c if c!=0 else -1

nk=[]
for i in range(int(input())):
    nk.append(list(map(int,input().split())))
    print(chck(nk[i]))
    
# print(chck([1,2,5]))
# print(chck([0,-1,5]))
