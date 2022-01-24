

#AIM-WAP to concatenate dict. to new one

dict1={"nk1":1}
dict2={"nk2":11}
dict3={"nk3":111}
dict4={}
for n in (dict1,dict2,dict3):
    print(n)
    dict4.update(n)

print(dict4)
"""
================OUTPUT=======================
{'nk1': 1}
{'nk2': 11}
{'nk3': 111}
{'nk1': 1, 'nk2': 11, 'nk3': 111}
>>> 
"""
