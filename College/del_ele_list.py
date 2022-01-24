l=[]
p=[]
n=int(input("Enter no of elements to be added to the list : "))
print("Enter the elements :")
for i in range(0,n):
    m=int(input())
    l.append(m)
for j in range(0,n):
    if j!=0 and j!=4 and j!=5:
        p.append(l[j])
l=p        
print("The list after removing 0th,4th and 5th element =",l)
"""============================Output=============================
Enter no of elements to be added to the list : 7
Enter the elements : 0 1 2 3 4 5 6
The list after removing 0th,4th and 5th element = [1, 2, 3, 6]
================================================================="""
