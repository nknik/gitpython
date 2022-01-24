# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
c, v = 0, "aeiouAEIOU"
for i in n:
    if i in v:
        c += 1
print(c)
