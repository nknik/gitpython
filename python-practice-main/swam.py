import time
class swayam:
    def __init__(self):
        self.bride=[]
        self.groom=[]
        self.pair={}
        self.match()

    def match(self):
        for i in range(len(self.bride)):
            #print(i)
            for j in range(len(self.groom)):
                #print("J",j)
                #print(self.bride[0],"==",self.groom[0])
                #print(i,"==",j)
                if self.bride[0]==self.groom[0]:
                    self.pair[i]=self.bride[0]
                    self.bride.pop(0)
                    self.groom.pop(0)
                    #print(self.bride.pop(0),'+0',self.groom.pop(0))
                    #print(self.bride,'+0',self.groom)
                    
                    break
                else:
                    self.a=self.groom.pop(0)
                    self.groom.append(self.a)
            else:
                print(len(self.groom))
                exit()
    def getdata(self):
        self.n=int(input())
        for i in range(0,self.n):
            self.bride.append(input())
        for i in range(0,self.n):  
            self.groom.append(input())
        self.match()    

if __name__ == "__main__":
    a=time.clock()
    n=swayam()
    n.getdata()
    print(n.pair)
    print(len(n.groom,))
    print(time.clock()-a)