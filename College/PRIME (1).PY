#AIM-WAP pp to chck prime
nk=int(input("ener a number"))
count=0
print("number->",nk)
def chck():
    global nk
    global count
    for n in range(1,nk):
        if nk%n==0:
           #print(nk,"is not prime")
            count+=1
        
if count==0:
    print(nk,"is  prime")
else:
    print(nk,"is not prime")
    
chck()

"""==================OUTput===============
ener a number9
number-> 9
9 is  prime
====================================="""
        
