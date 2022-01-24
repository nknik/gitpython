n=int(input("enter"))
if n <0 :
    print("Wrong Input")    
d=[]
for i in range(1,n+1):
    if n%i==0 :
        print(i,end=" ")