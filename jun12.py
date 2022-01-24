class Volcano:
    def __init__(self,name,country,elvation,area,last):
        self.name=name
        self.country=country
        self.elvation=elvation
        self.area=area
        self.last=last
        if last==2021:
            self.status='Active'
        elif 1996<last<2021:
            self.status="High probability"    
        elif 1971<last<1996:
            self.status="Low probability"
        else:
            self.status="Inactive"    
def volcanolist(nk,c,name):
    a=[]
    b=[]    
    for i in nk:
        if i.name.lower()==name.lower():
            a.extend([i.name,i.country,i.last])
        if i.country.lower()==c.lower():
            b.extend([i.name,i.country,i.last,i.status])
    if a!=[]:
        print(*a,sep="\n")
    else:
        print("no volcqno waliline tak")    
    if b!= []:
        print(*b,sep="\n")        
    else:
        print("no volcqno waliline tak")    
    pass
if __name__=="__main__":
    nk=[]
    for i in range(int(input())):
        a=input()
        b=input()
        c=int(input())
        d=int(input())
        e=int(input())
        nk.append(Volcano(a,b,c,d,e))
    c=input()
    a=input()
    volcanolist(nk,c,a)    
