class Subject:
    def __init__(self, code,name,credit,teacher,subavg):
        self.code=code
        self.name=name
        self.credit=credit
        self.teacher=teacher
        self.subavg=subavg

class grade:
    def __init__(self,grade,listt):
        pass        
        self.grade=grade
        self.Listt=listt
if __name__ == "__main__":
    pass
    ppp = []
    p=[]
    m=0
    mm=0
    for i in range(int(input())):
         code=input()
         name=input()
         credit=int(input())
         teacher=input()
         subavg=float(input())
         ppp.append(Subject(code,name,credit,teacher,subavg))
         p.append(subavg)
         if credit>m:
             m=credit
             mm=ppp[i]
if mm!=0:
    print(mm.code,mm.name,mm.credit,mm.teacher,mm.subavg,sep='\n')
else:
    print("nai wli line")    
p.sort()
print(*p,sep='\n')    