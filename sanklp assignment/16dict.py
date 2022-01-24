"""Q.16 Write a python program to use of any five method's of Dictionary."""
a = {1: 100, 2: 200, 3: 300}
b = a.copy()
print("first dict", a, "2nd dict", b, sep="\n")
b.clear()
print("first dict", a, "2nd dict", b, sep="\n")
print(a.fromkeys([4, 5]))
print("get value from dict", a.get(1, 0))
print(a.items())
print(a.keys())
print(a.values())
"""
=================================output==========================
first dict
{1: 100, 2: 200, 3: 300}
2nd dict
{1: 100, 2: 200, 3: 300}
first dict
{1: 100, 2: 200, 3: 300}
2nd dict
{}
{4: None, 5: None}
get value from dict 100
dict_items([(1, 100), (2, 200), (3, 300)])
dict_keys([1, 2, 3])
dict_values([100, 200, 300])
=================================output==========================
"""