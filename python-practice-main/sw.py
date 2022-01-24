aa = []
a = int(input())
aaa = []
if len(str(a)) == 2:
    for i in range(1, a):
        for j in range(1, a):
            if i*j == a:
                aa.append([i, j])
                aaa.append(i+j)
elif len(str(a)) == 3:
    for i in range(1, a):
        for j in range(1, a):
            for k in range(1, a):
                if i*j*k == a:
                    aa.append([i, j, k])
                    aaa.append(i+j+k)
# print(len(str(a)))
if len(aa) == 0:
    print("invalid")
else:
    for i in aa[aaa.index(min(aaa))]:
        print(i, end=" ")
