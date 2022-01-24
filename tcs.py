n = input()
if 0 < int(n) < 1000000:
    if n[-1] == "0":
        print(n)
    else:
        nn = int(n)
        if int(n[-1]) > 5:
            print(nn + (10 - int(n[-1])))
        else:
            print(nn - int(n[-1]))

else:
    print("out of range wali line")
# ////
nk = input()
aa = ["N", "E", "S", "W"]
n = 0
for i in nk:
    if i == "L":
        n = n - 1
    else:
        n = n + 1
print(aa[n % 4])
