import re
user=input("enter your ubantu username")
file=input("enter your terminal o/p file name")
# user,file="nikhil-nk","samba.txt"
regx="^"+user+".*"
filee=open(file,"r",encoding='UTF8')
new=open(str(file)+"-extract.txt","w")

for i in filee:
    if re.search(regx,i) is not None:
        new.write(i)
        print(i)
new.close()        
filee.close()        