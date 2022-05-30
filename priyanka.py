# a=input("enter char to match")
a="a"
aa=0
strr="ajgbdfhajkbfhkabkhdbhkbahkbdefkvhbdkab"
str2="snjdjhbfnsjksbnvjkbndskjbnscxjknkjcnzxczznaaa"
for i in strr+str2:
    if i==a:
        aa+=1
print(aa,"count")    

def dup(str1,str2):
    c=0
    for i in str1:
        if i in str2:
            c+=1
    return c 

print(dup("abcdef","defigab"))

def dupp(str1):
    c=""
    for i in str1:
        if i not in c:
            c+=i
    return c 

print(dupp("aaddadadabcdef"))