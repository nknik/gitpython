pal = lambda x: x == x[::-1]
a = ["nikhil", "aaaaaaaaaa", "nnknn", "nn", "n", "aba", "bvb"]
a = list(filter(pal, a))
print("pallidrom extracted", a)
aa = {}
for i in a:
    aa[len(i)] = aa.get(len(i), []) + [i]
n = [print(i, "->", j, sep=" ") for i, j in sorted(aa.items())]
print(n)
# ////////////////////////max profit///////////////////////
nn = [1, 2, 3, 4, 9, 8]
# nn=int(input())
# nn=list(map(int,input().split()))
sum = i = j = 0
sum += nn[i]
while j < len(nn):
    if nn[i] < nn[j] and nn[j] % nn[i] == 0:
        sum += nn[j]
        i = j
    j += 1
print(sum)
class nikhil(object):
    @classmethod
    def nkk(cls,input1,input2):
        nk=""
        for i in input1:
            if i!=input2:
                nk+=i
        return nk        
    @classmethod
    def nk(cls,input1,input2):
        return 'yes' if sorted(input1)==sorted(input2) else 'no'        
    @classmethod
    def nik(cls,input1,input2,input3):
        return (input1**input2)%input3      
    @classmethod
    def niik(cls,input1):
        def sum(n):
            sum = 0
            for digit in str(n):  
                sum += int(digit)       
            return sum    
        nk=1
        while nk:
            if nk%input1==0 and nk!=input1 and sum(nk)==input1 :
                num=0
                nkk=nk
                if num == nk:
                    return nk 
                    break  
                return nk
            nk+=1 
        return -1   
  
print(nikhil.nkk("Lord of rings","o"))    
print(nikhil.nk("abc","cbaa"))    
print(nikhil.nk("beast","yeast"))    
print(nikhil.nik(2,10,1025))    
print(nikhil.niik(9))   
print(nikhil.niik(10))   
# print(sum(19))   
# a=12345 
# aa=sum(list(map(int,str(a).strip())))
print(1==1.0)
numbers = [1,2,3,4,5,1,4,5]
  
# start parameter is not provided
# Sum = sum(numbers)
def summ(n):
    sum=0
    while n!=1:
        sum=sum+(n%10)
        n/=10
        print(n,sum)
    return sum    
print(1%10)