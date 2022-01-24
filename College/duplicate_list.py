l=[]
p=[]
n=int(input("Enter no of elements to be added to the list : "))
print("Enter the elements :")
for i in range(0,n):
    m=int(input())
    l.append(m)
for i in l:
    if i not in p:
        p.append(i)
print("Tne new list after removing duplicates =",p)
