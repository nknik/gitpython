l=[]
n=int(input("Enter no of elements to be added to the list : "))
print("Enter the elements :")
for i in range(0,n):
    m=int(input())
    l.append(m)
small,large=l[0],l[0]    
for i in l:
    if i<=small:
        small=i
    if i>=large:
        large=i
print("Smallest no in list =",small)
print("largest no in list =",large)
"""=============================Output=============================
Enter no of elements to be added to the list : 5
Enter the elements : 1 2 3 4 5
Smallest no in list = 1
largest no in list = 5
================================================================"""
