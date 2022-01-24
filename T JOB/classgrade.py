#!/bin/python3

import math
import os
import random
import re
import sys


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Student:
    def __init__(self, r, n, m):
        self.r = r
        self.n = n
        self.m = m

    def calculate_percentage(self):
        return sum(self.m) // len(self.m)

    def find_grade(self):
        self.nk = sum(self.m) // len(self.m)
        if self.nk >= 80:
            return "A"
        elif self.nk >= 60:
            return "B"
        elif self.nk >= 40:
            return "C"
        else:
            return "F"


if __name__ == "__main__":
    roll = int(input())
    name = input()
    count = int(input())
    marks = []
    for i in range(count):
        marks.append(int(input()))
    s = Student(roll, name, marks)
    print(s.calculate_percentage())
    print(s.find_grade())