#AIM-WAP to calculate no of upper case n lower case 
nk=input("enter a number")
ucount=0
lcount=0

def upper():
    global ucount
    for n in nk:
        if n.isupper():
            ucount+=1
def lower():
    global lcount
    for k in nk:
        if k.islower():
            lcount+=1
    
    
    
          
upper()
lower()
print("number of upper case",ucount)
print("number of lower case",lcount)



"""============================OUTPUT=================
enter a numberNiKhIl
number of upper case 3
number of lower case 3
======================"""
