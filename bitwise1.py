# nrfzh
nk="abcdefghijklmnopqrstuvwxyz"
print(nk)
n=input()
k=[]
for i in range(len(n)):
    print(k)
    k+=nk[nk.find(n[i])+ 2 if i == 25 else 1 if i==24 else 1]
print("".join(k))    
    