""""Q.17 Exercise-1: mydict ("bread":25,"cookies":10,"chipes":15) Write a python program to gives 10% discount on each value and display other dictionary after discount."""
mydict = {"bread": 25, "cookies": 10, "chipes": 15}
for i in mydict:
    mydict[i] -= mydict[i] * 0.1
print(mydict)

"""
===========================================output=======================

{'bread': 22.5, 'cookies': 9.0, 'chipes': 13.5}
===========================================output=======================
"""