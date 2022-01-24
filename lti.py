 def binary(i):
     r=str(0)
     while(i):
         x=str(i%2)
         if(x=='1' and r[-1]=='1'): #two consecutive X are not possible 
             return None
         else:
             r=r+str(x)
         i=i/2
     return r    
 m=3 #input
 l=[]
 for i in range(0,2**m):
     l.append(binary(i)) #converted the number to binary
 print(l)
 c=0 #count possible plot available
 for i in l:
     if i:
         c=c+1
 print(c*c) #both side of the
 from itertools import permutations
 class nik:
     @classmethod
     def usee(cls,input1):
         from itertools import product
         M=input1
         cnt = 0
         l = []
         for w in product(['x','y'], repeat=input1):
             tmp = ''.join(w)
             if 'xx' not in tmp:
                 l.append(tmp)
                 cnt += 1
         return (cnt*cnt)
 print(nik.usee(3) )       
 print(nik.usee(2) )       
 print(l)
 nk=[8.35,7.55,6.41,6.78,5.55,7.60,6.24,7.75]
 n=float(input("enter"))
 while n!=-1:
     nk.append(n)
     n=float(input("enter"))  
 print(sum(nk)/8)
 print(19&7)
 print(8&4)
 def garry(num) :
     result = 0
     i = 2
     while i<= ((num)**(1/2)) :
         if (num % i == 0) :
             if (i == (num / i)) :
                 result = result + i
             else :
                 result = result +  (i + num/i)
         i = i + 1
     return int(result + 1)
 num =int(input())
 nk=garry(num)
 nkk=garry(nk)
 if num==nkk:
     print(1)
 else:
     print(0)    




 def garrysandhu(nk1,nk2):
     return bin(int(nk1,2)+int(nk2,2))[2:]

 nk1=input()
 nk2=input()
 print(garrysandhu(nk1,nk2))

 nk1=str(num1)
 nk2=str(num2)
print(bin(102))
def fact(n):
    nk=1
    for i in range(1,n+1):
        nk*=i
    return nk 
print(fact(9))       
 nk=[]
 nkk=[]
for i in range(int(input())):
    nk=int(input())
    c=[]
    for i in range(0,nk):
        print(i,i+1)
        if i+i+1==nk and (i,i+1) not in c:
            c.append((i,(i+1)))
    print(len(c),c)        
 n,k=list(map(int,input().split()))
 c=0
 for i in range(n,k+1):
     if i==0:
         break
     c+=1
 print(c)    
    nikk=lambda nk:math.floor(nk/12)
import math
nk=int(input())
nk=list(map(int,input().split()))
def nik(input1,input2):
    nikkk=lambda nk:nk//12
    print(19//2)
    nk=list(map(nikk,input2))
    return sum(nk)
print(nik(5,[18,11,27,12,14]))
def countsub(text):
        def nik(str1, k):
            n = len(str1)
            res = 0
            cnt = [0] * 27
            for i in range(0, n):
                dist_count = 0
                cnt = [0] * 27
                for j in range(i, n):
                    if(cnt[ord(str1[j]) - 97] == 0):
                        dist_count += 1
                    cnt[ord(str1[j]) - 97] += 1

                    if(dist_count == k):
                        res += 1
                    if(dist_count > k):
                        break
            return res     
        count=0
        for i in range(1,len(text)):
            count+=nik(text,i)    
        print(count)    
        return count    
if __name__ == "__main__":
    str1 = "welcome"
    k = 3
    print(countsub(str1))