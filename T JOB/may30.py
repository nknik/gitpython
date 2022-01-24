def check(k):
    a=lambda x: True if x%2==0 else False
    k=list(map(a,k))
    if k.count(True)>1:
            return k.index(False)    
    else :
            return k.index(True)

for i in range(int(input())):
    n=int(input())
    k=map(int,input().split())
    print(check(k)+1)