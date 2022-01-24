from os import O_APPEND
from prettytable import PrettyTable
def matrix(word):
    x = PrettyTable(hrules=1, title="nks playfair")
    letter = "a b c d e f g h i/j k l m n o p q r s t u v w x y z".split()
    # word = word.replae('i','i/j')
    # word = word.replae('i','i/j')
    word = list(word.lower())
    word1 = []
    for i in word + letter:
        if i=='i' or i=='j':
            i='i/j'
        if i not in word1:
            word1.append(i)
    word1 = iter(word1)
    word = [[0 for i in range(5)] for j in range(5)]
    # word = []
    index={}
    for i in range(5):
        for j in range(5):
            word[i][j] = next(word1)
            index[word[i][j]]=[i,j]
    # x.title('playfair')
    for i in word:
        x.add_row(i)
    # print(*word, sep="\n")
    x.field_names = ["Nk1", "Nik2", "nk3", "nk4", "NK5"]
    print(x)
    index['i']=index['i/j']
    index['j']=index['i/j']
    # print(index,sep="\n")
    return word,index
def decrpt(index,mtrixx,w):
    # pass
    # print(len(word))
    # c=flag=0
    # w=[]
    e=''
    # for i in range(0,len(word),2):
    #     if len(word)%2==0 and word[i]==word[i+1]:
    #         flag=1
    # if flag:
    #     word+="x"    
    # while c<len(word):
    #     pass
    #     # print(word[c],end="")
    #     # print(word[c+1],end="\n")
    #     if word[c]==word[c+1]:
    #         w.append(f'{word[c]}x')
    #         c+=1
    #     else:
    #         w.append(f'{word[c]}{word[c+1]}')
    #         c+=2
    # w="".join(w)    

    # for i in word:
    #     if i in 'ij':
    #         i='i/j'
    #     w+=str(mtrixx[index[i][0]+1][index[i][1]])
    # print("nnnn",len(w))
    for i in range(0,len(w),2):
        # print(i)
        ar=index[w[i]][0]
        br=index[w[i+1]][0]
        ac=index[w[i]][1]
        bc=index[w[i+1]][1]
        arr=ar if ar!=0 else 5
        brr=br if br!=0 else 5
        acr=ac if ac!=0 else 5
        bcr=bc if bc!=0 else 5
        if ar==br:
            print("same row",'---' ,f"{w[i]}{w[i+1]}=>{mtrixx[ar][acr-1]}{mtrixx[ar][bcr-1]}")
            e+=f"{mtrixx[ar][acr-1]}{mtrixx[ar][bcr-1]}"
        elif ac==bc:
            print("same col",'---' ,f"{w[i]}{w[i+1]}=>{mtrixx[arr-1][ac]}{mtrixx[brr-1][ac]}")
            e+=f"{mtrixx[arr-1][ac]}{mtrixx[brr-1][ac]}"
        else :
            print("nothing same",'---' ,f"{w[i]}{w[i+1]}=>{mtrixx[ar][bc]}{mtrixx[br][ac]}")
            e+=f"{mtrixx[ar][bc]}{mtrixx[br][ac]}"
    return e,w
def encrpt(index,mtrixx,word):
    pass
    # print(len(word))
    c=flag=0
    w=[]
    e=''
    for i in range(0,len(word),2):
        if len(word)%2!=0 or word[i]==word[i+1]:
            flag=1
    if flag:
        word+="x"    
    while c<len(word):
        pass
        # print(word[c],end="")
        # print(word[c+1],end="\n")
        if word[c]==word[c+1]:
            w.append(f'{word[c]}x')
            c+=1
        else:
            w.append(f'{word[c]}{word[c+1]}')
            c+=2
    w="".join(w)    

    # for i in word:
    #     if i in 'ij':
    #         i='i/j'
    #     w+=str(mtrixx[index[i][0]+1][index[i][1]])
    print(w,"length of word=>",len(w))
    for i in range(0,len(w),2):
        # print(w[i])
        # if w[i]=='i' or w[i]=='j':
        #     w[i]='i/j'
        ar=index[w[i]][0]
        br=index[w[i+1]][0]
        ac=index[w[i]][1]
        bc=index[w[i+1]][1]
        arr=ar if ar!=4 else -1
        brr=br if br!=4 else -1
        acr=ac if ac!=4 else -1
        bcr=bc if bc!=4 else -1
        if ar==br:
            print("same row",'---' ,f"{w[i]}{w[i+1]}=>{mtrixx[ar][acr+1]}{mtrixx[ar][bcr+1]}")
            e+=f"{mtrixx[ar][acr+1]}{mtrixx[ar][bcr+1]}"
        elif ac==bc:
            print("same col",'---' ,f"{w[i]}{w[i+1]}=>{mtrixx[arr+1][ac]}{mtrixx[brr+1][ac]}")
            e+=f"{mtrixx[arr+1][ac]}{mtrixx[brr+1][ac]}"
        else :
            print("nothing same",'---' ,f"{w[i]}{w[i+1]}=>{mtrixx[ar][bc]}{mtrixx[br][ac]}")
            e+=f"{mtrixx[ar][bc]}{mtrixx[br][ac]}"
    return e,w
def mainn():
    word=input("enter word")
    key=input("enter key")
    mtrixx,index=matrix(key)
    print(len(index),index)
    if int(input("enter 1 for encrpt 0 for decrpt")):
        # print(mtrixx,sep="\n")
        aa=encrpt(index,mtrixx,word.lower())
        print("Modifed Word=>",aa[1],"Encrpted Word=>",aa[0])
        # print(mtrixx)
    else:    
        bb=decrpt(index,mtrixx,word.lower())
        print("Modifed Word=>",bb[1],"Encrpted Word=>",bb[0])
mainn()        