a=int(input('enter a number'))
b=int(input('enter a number'))
while(1):
    print('1.addition\n2.subtraction\n3.multiplication\n4.division\n')
    ch=int(input('enter your choice'))
    if(ch==1):
        print(a+b)
    if(ch==2):
        print(a-b)
    if(ch==3):
        print(a*b)
    if(ch==4):
        print(a/b)
    if(ch>=5):
        break
    if(ch<=0):
        break

"""
=========output======================
enter a number10
enter a number5
1.addition
2.subtraction
3.multiplication
4.division

enter your choice1
15
1.addition
2.subtraction
3.multiplication
4.division

enter your choice6
>>>
=====================================
"""