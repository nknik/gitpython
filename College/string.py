
"""Name: """


class string:
    def  __init__(self):
        self.str="str"
 
       
    def  getstr(self):
        self.str=input("Enter the string : ")
    def printstr(self):
        print("String is :",self.str.upper())
        x=len(self.str)
        print("Length of the string is :",x)
p=string()
p.getstr()
p.printstr()
