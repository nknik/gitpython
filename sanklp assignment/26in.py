"""
# INHERITANCE:

Q.26 Write a python program to display single inheritance"""

class A:
    def __init__(self):
        print("hello im a")
class B(A):
    def __init__(self):
        super().__init__()
        print("hello im B")
aa=B()       

"""
==========================================OUTPUT===========================
hello im a
hello im B
==========================================OUTPUT===========================

"""
