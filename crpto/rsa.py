encrpt=lambda m,e,n: m**e%n #e public key
decrpt=lambda c,d,n: c**d%n #d private key
privatee = lambda ei,n: ei%n # ei multiplicative inverse public key
publicc = lambda di,d,n: di%n #di multiplicative inverse private key
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m    
if __name__=="__main__":
    a=int(input("1 have p q encrpt \n2 have n\n3 find public\n4 find private  ")) 
    if a==1:
        p=int(input("enter p"))   
        q=int(input("enter q"))   
        n=p*q
        phi=(p-1)*(q-1)
        # e=publicc()
        m=int(input("enter plain text"))
        e=int(input("enter e public key"))
        ei=modinv(e,phi)
        d=privatee(ei,phi)
        print("private key is",d,"\n n is",n,"\nphi n is",phi)
        c=encrpt(m,e,n)
        print("cipher text is ",c)
        print("plain text is text is ",decrpt(c,d,n))
    if a==2:
        p=int(input("enter p"))   
        q=int(input("enter q"))   
        if p==0 or q==0:
            n=int(input("enter n"))
            for i in list(filter(lambda n: all(n%y != 0 for y in range(2,n)), range(2,n+1))):
                for j in list(filter(lambda n: all(n%y != 0 for y in range(2,n)), range(2,n+1))):
                    if i*j==n:
                        p,q=i,j
                        print("p and q are ",p,q)
                        break
                if p!=0 or q!=0:
                    break    
        else: n=p*q   
        phi=(p-1)*(q-1)
        print("phi is ",phi)
        e=int(input("enter q"))
        c=int(input("enter cipher"))
        ei=modinv(e,phi)
        print("mod inverse of e ",ei)
        d=privatee(ei,phi)
        print("private key is",d)
        m=decrpt(c,d,n)
        print("plain text is ",m)
    if a==3:
        p=q=0
        # n=int(input("enter n"))
        e=int(input("enter q"))
        if p==0 or q==0:
            n=int(input("enter n"))
            for i in list(filter(lambda n: all(n%y != 0 for y in range(2,n)), range(2,n+1))):
                for j in list(filter(lambda n: all(n%y != 0 for y in range(2,n)), range(2,n+1))):
                    if i*j==n:
                        p,q=i,j
                        print("p and q are ",p,q)
                        break
                if p!=0 or q!=0:
                    break    
        else: n=p*q   
        phi=(p-1)*(q-1)
        ei=modinv(e,phi)
        d=privatee(ei,phi)
        print("private key is ",d)

