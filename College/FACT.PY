# //TO FIND FACTORIAL OF A NUMBER

n=(int(input('enter a number')))
def fact():
    f=1
    for i in range (1,n+1):
      f=f*i
    print(f)
if(n>=1):
    fact();
elif(n==0):
    print('factorial of 0 is 1')
else:
    print('factorial does not exist')



# ==================OUTPUT================

# enter a number5
# 120    
    
        
    
