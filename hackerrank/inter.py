
def sortedSum(a):
    sum=0
    nk=[sorted(a[0:i]) for i in range(1,len(a)+1)]
    # for i in range(1,len(a)+1):
        # nk.append(sorted(a[0:i]))
    for i in nk:
        for j in i:
            sum+=(i.index(j)+1)*j
    return sum%((10**9)+7) 
print(sortedSum([9,5,8]))    