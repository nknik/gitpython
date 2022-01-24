# from sympy.ntheory.factor_ import totient

# n=323
# totient_n = totient(n) 
      
# print("phi({}) =  {} ".format(n, totient_n))
from math import gcd

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            # print(k,end=" ")
            amount += 1
    return amount
print(phi(323))    