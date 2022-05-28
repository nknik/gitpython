# aa=[a%x!=0 for x in range(2,a)]

# print(a)
n = 50
a = list(range(1, n + 1))
b = 0
aa = lambda a: all([a % x != 0 for x in range(2, a)])
while n != 1 :
    b += 1
    n = n- list(map(aa, a[1:])).count(True)
    a = list(range(1, n + 1))

b+=1
print(b)