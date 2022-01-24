def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)    
            print("=======")  
            for powers in range (1, modulo):
                print(f'{g}^{powers}mod{modulo}',pow(g, powers) % modulo)
            print("=======")
    return roots
privatee=lambda a,x,q:(a**x)%q
publicc=lambda a,x,q:(a**x)%q
key=lambda y,x,q : (y**x)%q
q=int(input("enter q"))
a=int(input("enter private key of a"))
b=int(input("enter private key of b"))
pr=primRoots(q)
print("primitive roots are",pr)
 
alp=int(input("enter primitive root else 0"))
alp=alp if alp else pr[0]
print("Ya=aplha^Xa modq")
ya=publicc(alp,a,q)
print("public key of A",ya)
print("Yb=aplha^Xb modq")
yb=publicc(alp,b,q)
print("public key of B",yb)
ka=key(yb,a,q)
kb=key(ya,b,q)
print("secret key of a=Xb^Xa mod q=>",ka)
print("secret key of b=Xa^Xb mod q=>",kb)
print("both are same" if ka==kb else "different")
