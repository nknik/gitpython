import json
import requests
class niknk:
    center_id=0
    name=0
    address=0
    state_name=0
    district_name=0
    block_name=0
    pincode=0
    lat=0
    long=0
    fromm=0
    to=0
    fee_type=0
    sessions=0

def get_books():
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=431601&date=06-05-2021' 
    # nk=requests.get(url).__dict__['_content']
    nk=requests.get(url).__dict__['_content']
    a=json.loads(nk.decode('utf-8'))
    # print(type(nk))
    c=""
    for i in a['centers'] :
        for j in i:
            if j=='sessions' or i==None:
                continue
            # print(j,i[j],end="\n")
            c+=f'{j} => {i[j]}\n'
        c+="====\n"    
    return c     
print(get_books())