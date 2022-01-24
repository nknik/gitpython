#Aim-WAP to to delete item from tuple & find length
nk2=(1,'n',3,3.14,3,4)
n=int(input("enter position to be deleted"))
print(nk2[:n]+nk2[n+1:])
print(len(nk2))

"""=========================OUTPUT==============
(1, 'n', 3, 3.14, 4)
6
>>> """
