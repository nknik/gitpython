a = {1: 1, 12: 22}
print(a)
n = dict()
n.get(11, 0)
nn = dict.fromkeys(range(11), 1)
a ={**a , 12:a.get(12,2)}
print(a)