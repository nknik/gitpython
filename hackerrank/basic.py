def decryptPassword(s):
    nk=''
    i=0
    print(s)
    while i < len(s) - 1:
        # print(s[i].isdigit())
        # i+=1 
        # print(s[i],s[i].islower(),s[i].isdigit())
        print(nk)
        i+=1
        if s[i].islower() :
            if i == len(s)-1 :
                if s[i+1].isupper():
                    # print(i)
                    nk+=s[i+1]+s[i]+'*'
                    i+=2
            else:
                nk+=s[i]
                i+=1    
        elif s[i].isdigit():
            nk=str(s[i])+nk+'0'
            i+=1
        else :
            i+=1        
    return nk       
print(decryptPassword("51Pa*0Lp*0e"))