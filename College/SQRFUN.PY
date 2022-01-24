'''AIM:-Write a program to print a list having values squares 1-13'''
def square(l1):
    s=1
    g=[]
    for i in l1 :
        s=i*i
        g.append(s)
    print('the list of square of no. in list',g)
l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print('the list is ',l)
square(l)
'''=====================================OUTPUT============================================
list is  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
the list of square of no. in list [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]'''
