""""# FUNCTIONS:

Q.22 Write a python program to calculate the simple interest by using function."""


def simple_interest(p, t, r):
    si = (p * t * r) / 100
    return si


print(f"simple interest is ,{simple_interest(80, 6, 8)}")
"""
========================OUTPUT========================
simple interest is ,38.4
========================OUTPUT========================
"""