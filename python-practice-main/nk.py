class encrnk:
    def __init__(self,n):
        self.item=list(n)
        self.temp=self.item
        self.result=[]
        #print(self.result)
        self.row1=1
        self.col1=3
        self.row2=3
        self.col2=3
        self.r=[[0,0,0]]
        self.A=[[0,0,0]]
        self.B=[[17,17,5],[21,18,21],[2,2,19]]
        while len(self.temp):
            self.A=[[self.convert(self.temp[0]),self.convert(self.temp[1]),self.convert(self.temp[2])]]
            del self.temp[0:3]
            #print(self.A)
            self.multiply()
        # self.getdataA()
        # self.getdataB()
        #self.multiply()
        #print(self.result)
        self.final()
    def final(self):
        self.nk=[self.converB(int(i)%26) for i in self.result] 
        print("".join(self.nk)) 
    def convert(self,nk):
        self.p={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        #print(self.p[nk])
        return self.p[nk]
    def converB(self,nk):
        self.p={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16:'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}    
        #print(self.p[nk])
        return self.p[nk]

    def multiply(self):
        # Matrix to store the result
        # self.r=[[0 for i in range(self.row1)]for j in range(self.col2)]
        if (self.row2 != self.col1) : 
            print("Not Possible") 
            return
        # Multiply the two  
        #print(self.r)
        for i in range(self.row1): 
            for j in range(self.col2) : 
                self.r[i][j] = 0
                for k in range(self.row2): 
                    self.r[i][j] +=self.A[i][k] * self.B[k][j]
        # Print the result  
        #print("Resultant Matrix: ") 
        #self.prin()
        #print(self.r)
        for i in self.r:
            for j in i:
                self.result.append(j)
        #self.result.append(self.r)

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
    n='paymoremoney'
    print("****************welcome to nks encrption**********")
    n=input("enter to encrpt=>").lower()
    print("encrpted succefully=>")
    if len(n)%3==0:
        nk=encrnk(n) 
    else:
        nk=encrnk(n+'a'*(3-len(n)%3))
    #print(list(n))