#AIM-student data

class nk:
    def __init__(self):
        self.n1=0
        self.n2=0
        self.n3=0
        self.n4=0
        self.n5=0
        self.n6=0
        self.n7=0
        self.n8=0
        
    def stddata(self):
             self.n1=input("name")
             self.n2=input("roll")
             self.n3=input("adress")
             self.n4=int(input("fess total"))
             self.n5=int(input("int1"))
             self.n6=int(input("int2"))
             self.n7=int(input("int3"))
             self.n8=self.n4-(self.n5+self.n6+self.n7)
             print("name=",self.n1)
             print("roll=",self.n2)
             print("address=",self.n3)
             print("total fees=",self.n4)
             print("insta1=",self.n5)
             print("insta2=",self.n6)
             print("insta3=",self.n7)
             
             print("balance",self.n8)
             print("++++++++++++++++++")
             
        
             
n=nk()
for k in range(1,5):
    n.stddata()
