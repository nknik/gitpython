class encrnk:
    def __init__(self,r1,c1,r2,c2):
        self.row1=r1
        self.col1=c1
        self.row2=r2
        self.col2=c2
        self.r=[]
        self.A=[]
        self.B=[]
        self.getdataA()
        self.getdataB()
        self.multiply()

    def multiply(self):
        # Matrix to store the result
        self.r=[[0 for i in range(self.row1)]for j in range(self.col2)]
        if (self.row2 != self.col1) : 
            print("Not Possible") 
            return
        # Multiply the two  
        for i in range(self.row1): 
            for j in range(self.col2) : 
                self.r[i][j] = 0
                for k in range(self.row2): 
                    self.r[i][j] +=self.A[i][k] * self.B[k][j]
        # Print the result  
        print("Resultant Matrix: ") 
        self.prin()

    def prin(self) :
        for i in self.r:  
            for j in i:  
                print(j, end = " ")
            print("\n")  
    def getdataA(self):
        self.A=[[0 for i in range(self.row1)]for j in range(self.col1)]
        for i in range(self.row1) :
            for j in range(self.col1) : 
                self.A[i][j] = int(input("[{}][{}]A/enter".format(i,j)))
    def getdataB(self):
        self.B=[[0 for i in range(self.row2)]for j in range(self.col2)]
        for i in range(self.row2) :
            for j in range(self.col2) : 
                self.B[i][j] = int(input("[{}][{}]B/enter".format(i,j)))

if __name__ == "__main__":
    nk=encrnk(3,3,3,3)
