#Aim-to perform all fuctions of tuple in python
nk=(1,2,3,4,5,6)
#len(tuple)
print("the length of tuple is-:>",len(nk))
#tuple(list)
nk1=[9,1,5,6,0,4,8,1,2,0]
print(nk1)
nk2=tuple(nk1)
print("Here list converted into tuple")
print(nk2)
#max(tuple)
print("max value in tuple",max(nk))
#min(tuple)
print("min value in tuple",min(nk))
"""=============================OUTPUT===================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
the length of tuple is-:> 6
[9, 1, 5, 6, 0, 4, 8, 1, 2, 0]
Here list converted into tuple
(9, 1, 5, 6, 0, 4, 8, 1, 2, 0)
max value in tuple 6
min value in tuple 1
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
======================================================================="""
