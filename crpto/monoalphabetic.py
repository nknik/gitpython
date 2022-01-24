def encrpt(msg, key):
    pass
    c = ""
    a = "a b c d e f g h i j k l m n o  p q r s t u v w x y z".upper().split()
    # print(len(msg), len(key))
    nk = lambda x: a.index(x)
    n = lambda x: key[x]
    print(*map(nk, msg.upper()))
    return "".join(list(map(n, map(nk, msg.upper()))))


def decrpt(msg, key):
    pass
    c = ""
    a = "a b c d e f g h i j k l m n o  p q r s t u v w x y z".upper().split()
    # print(len(msg),len(key))
    nk = lambda x: key.index(x)
    n = lambda x: a[x]
    return "".join(list(map(n, map(nk, msg.upper())))).lower()


msg = "assignment"
c = "LHHKVAXBAC"
key = "L M I P B Q V Z K R G Y X A E N W F H C J O D S U T"
print(msg, key, "cipher is", encrpt(msg, key.split()))
print("m is",c,key,decrpt(c,key.split()))