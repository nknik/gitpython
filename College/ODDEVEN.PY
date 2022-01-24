#AIM-WAP pp to separate even odd in list
nk=[1,2,3,4,5,6,7,8,9,10]
print(nk)
even=[]
odd=[]
def chck():
    global nk
    global even
    global odd
    for n in nk:
        if n%2==0:
           even.append(n)
        else:
            odd.append(n)
chck()
print("even->",even)
print("odd->",odd)
"""==================OUT===============
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even-> [2, 4, 6, 8, 10]
odd-> [1, 3, 5, 7, 9]
====================================="""
        
