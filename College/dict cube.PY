# //TO PRINT A DICTIONARY 

m=int(input('enter a value'))
n=int(input('enter a value'))
d=dict()
for i in range(m,n+1):
      d[i]=i*i*i
print(d)
"""
=============OUTPUT============
enter a value6
enter a value12
{6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728}
"""