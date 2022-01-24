#!/bin/python3

import math
import os
import random
import re
import sys


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Organisation:
    def __init__(self, o, e):
        super().__init__()
        self.o = o
        self.e = e

    def addEmployee(self, *n):
        self.e.append(n)

    def getEmployeeCount(self):
        pass
        return len(self.e)

    def findEmployeeAge(self, n):
        pass
        return (
            -1
            if [x[2] for x in self.e if n == x[1]] == []
            else [x[2] for x in self.e if n == x[1]][0]
        )

    def countEmployees(self, n):
        pass
        # print(self.e,n)
        return len([x for x in self.e if n < x[2]])


if __name__ == "__main__":
    employees = []
    o = Organisation("XYZ", employees)
    n = int(input())
    for i in range(n):
        name = input()
        id = int(input())
        age = int(input())
        gender = input()
        o.addEmployee(name, id, age, gender)

    id = int(input())
    age = int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))