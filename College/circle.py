
"""Name: Sakshi Dube,  Roll No. 73"""

class circle:
    
    def  __init__(self,r):
        self.r=r     
    def  area(self):
        area1=3.14*self.r*self.r
        print("Area of  circle:",area1)
    def peri(self):
        peri1=2*3.14*self.r
        print("Perimeter of circle :",peri1)

        
r=int(input("Enter the radius:"))
c=circle(r)
c.area()
c.peri()


"""
OUTPUT
Enter the radius:3
Area of  circle: 28.259999999999998
Perimeter of circle : 18.84
"""
