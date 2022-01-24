distance=int(input())
time=int(input())
cost=0
if distance <= 250 and time <=8:
    cost=2000
elif distance >250 and time <=8:
    cost=2000+(distance-250)*20
elif distance >250 and time >8:
    cost=2000+(distance-250)*20+(time-8)*100
elif distance <=250 and time >8:
    cost=2000+(time-8)*100
elif distance<1 or time<1:
    print("error")
if cost: print(cost)    
