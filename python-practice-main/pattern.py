def first(n):
    n+=1
    for i in range(n) if n >0 else range(n,1): 
        print(abs(i)*"*"+(n-i)*2*' '+abs(i)*"*",end="\n")
    for i in range(n-1,0,-1) if n >0 else range(n,-1): 
        print((n-i)*' '+abs(i)*"*"+abs(i)*"*"+(n-i)*' ',end="\n")
    
    # for i in range(n) if n >0 else range(n,1): print(abs(i)*"* ",end="\n")
first(6)    
# first(5)    
# first(3)    
# first(2)
# first(1)
#python pattern.py > pattern.txt & type pattern.txt