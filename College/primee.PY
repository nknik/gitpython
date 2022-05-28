l =[]
n=int(input("Enter No of elements in list"))
for p in range(0,n):
    m=int(input("Enter element to be added"))
    l.append(m)
c=0
for x in l:
    s=0
    for y in range(2,x):
        if (x % y) == 0:
            s=1
    #print(s)
    if s!=1:
           print(x, "is prime number")       
           c=c+1
print("No of prime numbers =",c)

"""===============================Output============================
Enter No of elements in list3
Enter element to be added1
Enter element to be added2
Enter element to be added3
1 is prime number
2 is prime number
3 is prime number
No of prime numbers = 3
====================================================================
"""