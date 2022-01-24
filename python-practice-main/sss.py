m=[80,130,100,80,0,110,120,140,70,80]
o=[]
q=[]
total=0
nk=1
while nk:
    oo=input()
    qq=input()
    c=input()
    m=input()
    if c=='y':
        o.append(int(oo))
        q.append(int(qq))
    else:
        break    
for i in range(len(o)):
    total=m[o[i]]*q[i]   
if total<1000:
    pass 
elif m=='y' :
    total-=0.05*total
elif total>1000 :
    total-=0.1*total
print(total)     
