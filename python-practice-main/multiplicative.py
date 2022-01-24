global b 
b=0
def modInverse(a, m) : 
    global b
    print(b)
    b=b+1
    a = a % m; 
    print(a)
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            print(b)
            b=b+1
            return x 
    return 1
  
# Driver Program 
a = 353
m = 1783
print(m%a)
print(modInverse(a, m))
print(b)