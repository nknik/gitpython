








# a=13
# a=1001
# a=15
#  a=int(input())
# aa=str(bin(a))[2:]
# if 0<a<1000:
#     if aa.count('1')%2==0:
#         print("Even Parity")
#     else:
#         print("Odd Parity")
# else:        
#     print("Wrong Input")


#=========================================================
h = 4
m = 10
def calcAngle(h,m):
        if (h < 0 or m < 0 or h > 12 or m > 60):
            return 'Wrong input'
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            h += 1;
            if(h>12):
                   h = h-12;
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m
        angle = abs(hour_angle - minute_angle)
        angle = min(360 - angle, angle)
        return str(format(angle, '.2f'))
        return str(round(angle,2))
# h = int(input())
# m = int(input())
print(calcAngle(h,m))
print(round(22/7,2))
print(round(22/7,2))







