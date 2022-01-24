#AIM-WAP to add & multi given string
total=1
result=0
nk=(1,2,3,4,5,6)
def mul():
    global total
    for n in nk:
        total*=n
def add():
    global result
    for k in nk:
        result+=k
mul()
add()
        
    
print("multiplication=",total)
print("addition=",result)
"""============================OUTPUT=================
multiplication= 720
addition= 21
======================"""
