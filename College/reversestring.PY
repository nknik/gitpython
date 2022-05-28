#AIM-WAP to reverse a string
nk=input("enter a string")
nk1=[]
def rev():
    global nk
    global nk1
    nk1=nk[::-1]
          
rev()    
print("og string->",nk)
print("reversed string->",nk1)

"""============================OUTPUT=================
enter a stringnikhil
og string-> nikhil
reversed string-> lihkin
======================"""
