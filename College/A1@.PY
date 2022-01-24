s=input('enter a string ')
a=0
d=0
c=0
if(s.isalpha()=='true'):
    a=a+1
elif(s.isdigit()=='true'):
    d=d+1
else:
    c=c+1
print("alphabets,digits and other characters in the string are")
print(a,d,c)
