from rsa import modinv
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
                pass
                # print(f'{g}^{powers}mod{modulo}',pow(g, powers) % modulo)
            print("=======")
    return roots
q=int(input("enter q"))
apha=int(input("enter alpha"))
k=int(input("enter k"))
m=int(input("enter m"))
a=int(input("enter 1 XA 2 YB"))
if a==1:
    xa=int(input("enter Xa"))
    ya=(apha**xa)%q
    print(ya,"ya")
if a==2:
    ya=int(input("enter ya"))
    for i in range(1,q):
        if ya==(apha**i)%q:
            xa=i
            break
if True:        
    if apha in primRoots(q):
        print(f"{apha} s pmtive r0ot of {q} ")
    if gcd(k,q-1)==1: print(k,"and",q-1,"are coprime")    
    aa=modinv(k,q)%(q-1)
    print("k**-1%(q-1)",aa)
    s1=(apha**k)%q
    s2=modinv(k,q-1)*((m-xa*s1)%(q-1))
    print(s1,s2)
    v1=apha**m%q
    v2=(ya**s1)*(s1**s2)%q
    print(v1,v2,"are same" if v1==v2 else "diff")