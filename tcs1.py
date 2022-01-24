x = [3,5,2,4]
nk=[9,6,3]
# x = [3,10,4,6]
# nk=[20,11,15]

# x k m n
# x.append(int(input()))
# x.append(int(input()))
# x.append(int(input()))
# x.append(int(input()))
# nk = list(map(int, input().split()))
a = [0, 0, 0]
for i in range(len(nk)):
    for j in range(len(x)):
        for k in range(len(x)):
            if j != k:
                # print(x[j],x[k],nk[i])
                if x[j] + x[k] == nk[i]:
                    a[i] = 1
                    x[j]=0
                    x[k]=0
                    # x.pop(x.index(x[j]))
                    # x.pop(x.index(x[k]))
print(*a, sep=" ")
