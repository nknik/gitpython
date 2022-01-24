a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
s=1
print("+ for addition , - for substraction")
print("* for multiplication , / for division")
print("press n for exit")
##choice=input("Enter opertion to be performed")
while(s==1):
    choice=input("Enter opertion to be performed")
    if(choice=="n"):
        s=0
    elif(choice=="+"):
        print(a+b)
    elif(choice=="-"):
        print(a-b)
    elif(choice=="*"):
        print(a*b)
    elif(choice=="/"):
        print(a/b)    
"""=========================Output=============================
Enter the first number2
Enter the second number1
+ for addition , - for substraction
* for multiplication , / for division
press n for exit
Enter opertion to be performed+
3
Enter opertion to be performedn
============================================================"""
