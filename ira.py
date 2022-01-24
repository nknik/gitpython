class passenger:
    def __init__(self,idd,name,age):
        self.id=idd
        self.name=name
        self.age=age
class ticket:
    def __init__(self,idd,tickettype,traveltype,trainnumber,traveldest,passengerlist,traintuple,fare):
        self.idd=idd
        self.tickettype=tickettype
        self.traveltype=traveltype
        self.trainnumber=trainnumber
        self.traveldest=traveldest
        self.passengerlist=passengerlist
        self.traintuple=traintuple()
        self.fare=fare
if __name__=="__main__":
    trainlist=('MUM-GOA','DEL-MUM','LKO-KOL','MUM-DEL','GOA-MUM','KOL-LKO')
    trainid=(1221,2331,7654,5690,5463,9854)
    pricegen=(100,200,300,400,500,600)
    tatkalpricegen=(700,800,900,1000,1100,1200)
    ticketdate='2020-12-09'
    for i in range(int(input())):

