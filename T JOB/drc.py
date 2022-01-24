n = 56  # int(input("enter"))
nn = [[x,y] for x in range(1, n) for y in range(1,n) if x*y == n]
l = len(str(n))
nk=[]
print(l)
if l==2:
    for i in nn :
        for j in nn:
            if i*j==n:
                nk.append([i,j])
nk=sorted(nk)
print(nk)
print(f'{nk[0][0]}{nk[0][1]}')