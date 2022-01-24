l=[]
add,multi=0,1
n=int(input("Enter no of elements to be added to the list : "))
print("Enter the elements :")
for i in range(0,n):
    m=int(input())
    l.append(m)
for i in l:
    add=add+i
    multi=multi*i
print("Addition of numbers in list =",add)
print("Multiplication of numbers in list =",multi)    
"""==========================Output============================
Enter no of elements to be added to the list : 4
Enter the elements : 1 2 3 4
Addition of numbers in list = 10
Multiplication of numbers in list = 24
============================================================"""



    

