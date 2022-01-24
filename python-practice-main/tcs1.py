"""Maximum Distance Marathon Runner
A marathon is a long-distance race with an official distance of 42.195 kilometers (26 miles 385 yards), usually run as a road race or footrace.

A local marathon was organized at Pune. The distance actually covered by the participants has been recorded in an array R[] which is an integer array holding the values in kilometers. If there are N number of participants who started running at a particular time, then the size of R is N. The participants should cover a distance more than 0.0 km to get recorded in array R[].

Find the maximum distances covered by 3 highest racers excluding finishers. If there are only one or two racers excluding finishers, give their distances covered.

R[] will be Input float array. Write a code to take Input array R[], and return 3 maximum distances excluding Finishing Distance d, d = 42.195 km



Example 1:

Input Values

Enter the distances covered by racers in Marathon (Kilometers) please

(press q to terminate):

42.195

42.195

42.195

33.25

40

41.2

38.9

37.5

q



Output Values

Highest Distance excluding Finishers:

[41.2, 40, 38.9]



Example 2:

Input Values

Enter the distances covered by racers in Marathon (Kilometers) please

(press q to terminate):

33.33

42.9

39.56

-35.6

42.195

q

Output Values

Highest Distance excluding Finishers:

Invalid Input."""

a = []
while True:
    b = input()
    if b == 'q':
        break
    elif float(b) >= 42.195:
        pass
    else:
        a.append(float(b) if float(b) % 1 != 0 else int(b))
a.sort(reverse=True)
for i in a:
    if str(i).isdigit() != True and i < 0:
        print("Invalid Input")
        break
else:
    print(a[0], a[1], a[2])
