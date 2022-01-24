# nk=[4,8,6,12]
# nk=list(map(int,input().split()))
# nk.sort()
# sum=0

# print(nk)
def nk(fileSizes):
    fileSizes = list(fileSizes)
    s = 0
    fileSizes.sort()
    while len(fileSizes) > 1:
        fileSizes[0] = fileSizes[0] + fileSizes[1]
        fileSizes.pop(1)
        s += fileSizes[0]
    print(s)    
    return s

def nkk(n):
    s=0
    for i in n:
        s+=min(i)


print(nk([4, 8, 6, 12]))
