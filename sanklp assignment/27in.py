""" Q.27 Write a python program to display multiple inheritance"""

class A:
    def __init__(self):
        print("hello im a==")
class B:
    def __init__(self):
        print("hello im B==")
class C(A,B):
    def __init__(self):
        super(A,self).__init__()
        super(B,self).__init__()
        print("hello im C==")
aa=C()        
"""
==========================================OUTPUT===========================
hello im B==
hello im C==
==========================================OUTPUT===========================
"""
