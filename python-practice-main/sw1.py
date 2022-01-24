n=int(input())
nn=[int(input()) for i in range(n)]
if n==1:
    print("invalid")
else:    
    for i in sorted(nn)[:2]:
        print(i,end=" ")