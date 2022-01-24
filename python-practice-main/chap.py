import re
hand = open ('regex_sum_777295.txt')
lst = list()
stuff=[]
for line in hand:
    line = line.rstrip()
    stuff += re.findall('[0-9]+', line) 
stuff1=[int(x) for x in stuff]
print(sum(stuff1))