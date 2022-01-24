import re
import datetime as d
# print(re.search("cat","i do likes cat"))
# a=re.search("cat","i do likes cat")
# print(type(a))
# print(dir(re))
# print(help(re))
# #print(help())
# print(dir(d))
# #print(help(d))
def A_welcome():
    """WELCOME to nikhils Timestamp Module"""



def timestamp():
    """timestamp()=>gives whole timestamp"""
    date=dict()
    date['timestamp']="Date=>"+str(d.datetime.now())[:10][-2:]+"-"+str(d.datetime.now())[:10][-5:-2]+str(d.datetime.now())[:4]+"  Time=>"
    if int(str(d.datetime.now())[10:13])>12:
        date['timestamp']+="  "+str(int(str(d.datetime.now())[10:13])-12)+' PM'+str(d.datetime.now())[13:19]
    elif int(str(d.datetime.now())[10:13])==12:
        date['timestamp']+="  "+str(int(str(d.datetime.now())[10:13]))+' PM'+str(d.datetime.now())[13:19]
    else:
        date['timestamp']+="  "+str(int(str(d.datetime.now())[10:13]))+' AM'+str(d.datetime.now())[13:19]
    return date['timestamp']

def Date():
    """Date()=>gives time in AM/PM"""
    return "Date=>"+str(d.datetime.now())[:10][-2:]+"-"+str(d.datetime.now())[:10][-5:-2]+str(d.datetime.now())[:4]
# a=timestamp()   
# print(a)
def Time():
    """Time()=>gives time in AM/PM"""
    date=dict()
    date['timestamp']="Time=>"
    if int(str(d.datetime.now())[10:13])>12:
        date['timestamp']+="  "+str(int(str(d.datetime.now())[10:13])-12)+' PM'+str(d.datetime.now())[13:19]
    elif int(str(d.datetime.now())[10:13])==12:
        date['timestamp']+="  "+str(int(str(d.datetime.now())[10:13]))+' PM'+str(d.datetime.now())[13:19]
    else:
        date['timestamp']+="  "+str(int(str(d.datetime.now())[10:13]))+' AM'+str(d.datetime.now())[13:19]
    return date['timestamp']
# print(Time())