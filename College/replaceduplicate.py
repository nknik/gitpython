def replace(s,n,k):
    return "".join([x if x!=n else k  for x in s])
s="restart"
# s=input("Enter a String : ")
a=s[0]
# s1=s.replace(a,"$")
s1=replace(s,a,"$")
s2=a+s1[1:]
print(s2)
[print(s[x],end="") for x in range(len(s)-1,-1,-1)]
"""===================Output=====================
Enter a String : restart
resta$t
=============================================="""
