#Aim-WAP to add item in tuple
print("add item in tuple")
#using concatination
nk2=(1,'n',3,3.14)
nk2=nk2+(4,)
print(nk2)
#using slicing
nk2=nk2[:3]+(6,7,8,9)
print(nk2)
#using conversion tuple->list
nk1=list(nk2)
print(nk1)
nk1.append("list")
nk3=tuple(nk1)
print(nk3)
"""=========================OUTPUT==============
add item in tuple
(1, 'n', 3, 3.14, 4)
(1, 'n', 3, 6, 7, 8, 9)
[1, 'n', 3, 6, 7, 8, 9]
(1, 'n', 3, 6, 7, 8, 9, 'list')ss
>>> 
============================================="""
