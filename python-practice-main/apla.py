alpha = list('abcdefghijklmnopqrstuvwxyz')
t ='whoyouare'
tt=[5281,8313,10206,10670,10206,3205,1,187,7258]
# for i in t:
#     tt.append(alpha.index(i)+1)
nk=[]
for i in tt:
    nk.append(alpha[i%26-1])
print(nk)    
