# nn=[[3,2,5],[8,9,1],[4,7,6]]
# k=3
# kk=[[1,1,1],[1,1,1],[1,1,1]]
n = int(input())
k = int(input())
nn = [list(map(int, input().split())) for i in range(k)]
kk = [list(map(int, input().split())) for i in range(k)]
nik = []
for i in range(len(nn)):
    inn = nn[i].index(min(nn[i]))
    # print(min(nn[i])-kk[i][inn])
    nik.append(min(nn[i]) - kk[i][inn])
print(sum(nik) + 1)
# 3
# 3
# 3 2 5
# 8 9 1
# 4 7 6
# 1 1 1
# 1 1 1
# 1 1 1
# 5