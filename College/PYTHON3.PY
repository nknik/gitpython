

#AIM-WAP to check if given key already exixt in dict or not
nk={'nk1': 1, 'nk2': 11, 'nk3': 111}
def chck(n):
    if n in nk:
        print("key is present")
    else:
        print("key is not present")
        
#n=input("enetr variable to chck")
chck("nk1")
chck("nk")
chck("nk3")
"""
================OUTPUT=======================
key is present
key is not present
key is present
"""
