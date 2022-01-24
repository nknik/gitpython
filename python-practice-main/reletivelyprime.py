def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

print(coprime(14,15)) #Should be true
print(coprime(14,28)) #Should be false