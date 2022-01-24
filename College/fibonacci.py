a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a)
print(b)
for p in range(1,n-1):
    c=a+b
    a=b
    b=c
    print(c)
"""=========================Output=============================
Enter the first number of the series 0
Enter the second number of the series 1
Enter the number of terms needed 5
0
1
1
2
3
============================================================"""
