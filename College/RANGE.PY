#AIM-WAP to chck the given number is in range or not
nk=int(input("enter a number"))
n=int(input("enter starting"))
k=int(input("enter ending "))

def chckrange():
    global nk
    global n
    global k
    if (nk>n&nk<k):
            print(nk,"number is in range")
    
          
chckrange()    



"""============================OUTPUT=================
enter a number23
enter starting1
enter ending 30
23 number is in range
======================"""
