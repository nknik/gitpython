#Aim-WAP to check element exixt in tuple or not
nk2=(1,'n',3,3.14,3,4)
s=0
n=int(input("enetr elements to be searched"))
for i in nk2:
    if(i==n):
        s=1
if(s==0):
    print("element not exist in tuple")
else:
    print("element exist in tuple")
    

"""=========================OUTPUT==============
enetr elements to be searched3
element exist in tuple
>>> """
