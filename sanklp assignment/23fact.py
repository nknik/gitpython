"""Q.23 Write a python program accepts number from user and calculate a factorial by using

function."""


def facty(a):
    aa = 1
    for i in range(1, a + 1):
        aa *= i
        print(aa)
    return aa


print(f"factorial of 20 is {facty(6)}")
"""
==============================OUTPUT================================
factorial of 20 is 720
==============================OUTPUT================================
"""

