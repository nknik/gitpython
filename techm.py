input2=[]
for i in range(int(input())):
    input2.append(int(input()))
return max([input2[i]-input2[i+1] for i in range(len(input2)-1) ])
print(n)