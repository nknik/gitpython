>>> import json
>>> with open('people.json', 'r') as people_json:
...     people = json.load(people_json)
... 
>>> print(people)
[{'name': 'Sabrina Green', 'username': 'sgreen', 'phone': {'office': '802-867-5309', 'cell': '802-867-5310'}, 'department': 'IT Infrastructure', 'role': 'Systems Administrator'}, {'name': 'Eli Jones', 'username': 'ejones', 'phone': {'office': '684-348-1127'}, 'department': 'IT Infrastructure', 'role': 'IT Specialist'}, {'name': 'Melody Daniels', 'username': 'mdaniels', 'phone': {'cell': '846-687-7436'}, 'department': 'User Experience Research', 'role': 'Programmer'}, {'name': 'Charlie Rivera', 'username': 'riverac', 'phone': {'office': '698-746-3357'}, 'department': 'Development', 'role': 'Web Developer'}]



>>> import json
>>> 
>>> people = [
...   {
...     "name": "Sabrina Green",
...     "username": "sgreen",
...     "phone": {
...       "office": "802-867-5309",
...       "cell": "802-867-5310"
...     },
...     "department": "IT Infrastructure",
...     "role": "Systems Administrator"
...   },
...   {
...     "name": "Eli Jones",
...     "username": "ejones",
...     "phone": {
...       "office": "684-348-1127"
...     },
...     "department": "IT Infrastructure",
...     "role": "IT Specialist"
...   }
... ]
>>> people_json = json.dumps(people)
>>> print(people_json)
[{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]


>>> import requests
>>> response = requests.get('https://www.google.com')

>>> print(response.text[:300])
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="dZfbIAn803LDGXS9


    >>> response = requests.get('https://www.google.com', stream=True)
>>> print(response.raw.read()[:100])
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xdbz\x9b\xc8\x96\xbe\xcfS`\xf2\xb5-\xc6X\x02$t\xc28\xe3v\xdc\xdd\xee\xce\xa9\xb7\xdd;\xe9\x9d\xce\xf6W@\t\x88\x11`@>D\xd6\x9b\xce\xe5<\xc3\\\xcd\xc5\xfc\xab8\x08\xc9Nz\x1f.&\x8e1U\xb5j\xd5:\xfc\xb5jU\x15\x87;^\xe2\x16\xf7)\x97\x82b\x1e\x1d\x1d\xd2S'


>>> response.ok
True

>>> response.status_code
200


response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))


response = requests.get(url)
response.raise_for_status()


>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 