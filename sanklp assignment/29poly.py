"""Q.29 Write a python program to display operator polymorphism"""
class subject:
    def __init__(self,a):
        self.a=a
    def __add__(self,objj):
        return self.a+objj.a
aa=subject(10)
ab=subject(11)
print(aa+ab)
"""
==========================================OUTPUT===========================
21
==========================================OUTPUT===========================

"""
