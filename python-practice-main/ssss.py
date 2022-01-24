l = [0,50,100,40,200,300]
item = list(map(int,input().split()))
quan = list(map(int,input().split()))
c = input()
cost = 0
for i in range(len(item)):
    cost = cost + quan[i]*l[item[i]]
if cost>100 and c== 'y':
    cost = cost-cost*15/100
if cost>1000 and c!='y':
    cost = cost-cost*0.1
if max(item)>5:
    print('INVALID INPUT')
else:
    print(cost,'INR')