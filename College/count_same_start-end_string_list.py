l=[]
count=0
n=int(input("Enter no of strings to be added to the list : "))
print("Enter the strings :")
for i in range(0,n):
    m=input()
    l.append(m)
print("The strings whose first and last character are same are :")    
for i in l:
    if len(l)<2:
        print("Invalid String Input")
        exit
    else:
        if i[0]==i[len(i)-1]:
            print(i)
            count+=1
print("no.of strings whose first and last character are same =",count)
"""=============================Output=================================
Enter no of strings to be added to the list : 3
Enter the strings : vedant raghuveer rohan
The strings whose first and last character are same are : raghuveer
no.of strings whose first and last character are same = 1
===================================================================="""    
