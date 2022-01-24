#
n = 5
s = []
if n > 1 and n < 21:
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ss = str(i)+str(j)
            if ss not in s and ss[::-1] not in s:
                s.append(str(i)+str(j))
    print(len(s)//2)
    print(s)
else:
    pass
    print("Wrong Infrastructure")
