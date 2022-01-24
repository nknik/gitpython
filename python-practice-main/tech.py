# n=int(input("enter"))
t = 0
nn = [18, 11, 27, 12, 14]
# for x in range(n) : nn.append(int(input("enter")))
for i in nn:
    t += int(i/12) if i > 11 else 0
    print(t)
# [nodemon] clean exit - waiting for changes before restart
# [nodemon] restarting due to changes...
# [nodemon] starting `python tech.py`
# 1
# 1
# 3
# 4
# 5
# [nodemon] clean exit - waiting for changes before restart
