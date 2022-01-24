
# Aim : Program to find out the no. is odd or even

l=[]
n=int(input("Enter No of elements in list"))
print("Enter elements to be added")
for p in range(0,n):
    m=int(input("Enter : "))
    l.append(m)
for p in l:
    if p%2==0:
        print("%d is even no." %(p))
    else:
        print("%d is odd no." %(p))
"""===============================Output============================
Enter No of elements in list5
Enter elements to be added
Enter : 1
Enter : 2
Enter : 3
Enter : 4
Enter : 5
1 is odd no.
2 is even no.
3 is odd no.
4 is even no.
5 is odd no.
================================================================="""            
        
