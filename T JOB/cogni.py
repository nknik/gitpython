''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def check(one, two):
    m = len(one)
    n = len(two)
    i=j=0
    for a in range(len(two)):
        for b in range(len(one)) :
            # print(a,b)
            print(two[a],one[b])
            if two[a]==one[b]:
                j+=1
                break
    # while j < m and i < n:
    #     print(one[j],two[i])
    #     if one[j] == two[i]:
    #         j = j+1
    #     i = i + 1
    return j == m

def main():
    v=input()
    b=[]
    for i in range(int(input())):
        print("POSITIVE" if check(input(),v) else "NEGATIVE")
 # Write code here 

# main()
# print(check("crnas","coronavirus"))
====================================
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def prime(n):
    if n==2: return True
    for i in range(2,int((n**.5))+1):
        if n%i==0:
            return False
    else: return True        
def main():
    for i in range(int(input())):
        a,b=map(int,input().split())
        if a==b and prime(a):
            print(0)
        else:    
            nk=[x for x in range(a,b+1) if prime(x)]
            if nk!=[]:print(max(nk)-min(nk))
            else :print(-1)
 # Write code here 

main()
