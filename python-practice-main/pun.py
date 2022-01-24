# 
# a = 'tatkakakakll'
# a='nikhil'
a='opopapppppppppppppppppppppppppppppp'
# print(list(a))
a=input()
aa = ''
if len(a)<20:
    for i in a:
        # print(list(a).count(i))
        n=list(a).count(i)
        if n==1:
            aa=i
            print(aa)
    if aa=='':
        print("Exceptional String")
    else :       
        print(aa) 
else :
    print("Wrong Input")