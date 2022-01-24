

#AIM-build a pp to generate a print that contains a no. between one and x,x*x
nk=int(input("enetr number"))
n={x:x*x for x in range(1,nk+1)}
print(n)

"""
================OUTPUT=======================
enetr number4
{1: 1, 2: 4, 3: 9, 4: 16}
"""
