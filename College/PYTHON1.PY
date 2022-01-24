


class changestring :
    def __init__(self,a):
            self.a=a
    def makeupper(self):
            self.b=self.a.upper()
            print("upper case string",self.b)
    def makelower(self):
            self.c=self.a.lower()
            print("lower case string",self.c)
r=input("Enter the string")
c1=changestring(r)
c1.makeupper()
c1.makelower()


"""========output======
Enter the stringHAPPY
upper case string HAPPY
lower case string happy
==========================="""
