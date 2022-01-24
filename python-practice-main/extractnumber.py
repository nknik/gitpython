from re import *
txt="hi my roll number is #12"
def extract(t):
    no=findall("\d+",t)
    return no[0]
print(extract(txt))    