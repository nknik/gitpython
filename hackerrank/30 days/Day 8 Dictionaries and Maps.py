# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
p = dict()
for i in range(n):
    l = input().split()
    p[l[0]] = p.get(l[0], l[1])

while 1:
    try:
        q = input()
        if q in p:
            print(str(q) + "=" + str(p[q]))
        else:
            print("Not found")
    except:
        break
