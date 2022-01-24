# sweta tech mahindra 25 nov 20
import functools as n
def odd(nk):
    return True if nk%2!=0 else False
def even(nk):
    return True if nk%2==0 else False
def dub(aa,bb):
    """
    docstring
    """
    pass
    return aa-bb

a= [10,11,12,7,14]#[int(input()) for _ in range(int(input()))]#
b=sum(list(filter(odd,a))) -sum(list(filter(even,a)))
c= n.reduce(dub,a)
print(c,a)
"""
nodemon] starting `python tech1.py`
5
10
11
12
7
14
-18
[nodemon] clean exit - waiting for changes before restart
"""