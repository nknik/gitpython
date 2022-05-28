# //TO ACCEPT A LIST AND PRINT AFTER REMOVING EVEN NUMBERS

print('enter a list of integers ')
l=[int(x) for x in (input().split())]
print(l)
for i in (l):
    if(i%2==0):
        l.remove(i)
print("list after removing even numbers from it")
print(l)

"""
================OUTPUT=================
enter a list of integers 
0 1 2 3 4 5 6 7 8 9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list after removing even numbers from it
[1, 3, 5, 7, 9]

"""