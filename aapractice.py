a=list(range(5))
b=2
print(a,"hare krishna",b)
print(all(a))
print(any(a))
print(repr(22))
print(ascii(22))
print(bool(22))
print(divmod(3,2))
print(type(divmod(3,2)))
en=enumerate(a,start=5)
for i in en:
    print(i,type(i))
print(type(divmod(3,2)))
print([i for i in reversed(a)])
nn=4.5
print(round(nn))
# print(nn.ceil())
# print(floor(nn))
class test:
    a=0
    b=0
    c=0
    def __init__(self) -> None:
        super().__init__()
        self.name="nikhil"
        self.nam="nikhil"
        self.na="nikhil"
nk=test()
print(vars(nk))

nn=11111.1234567
print(f"{nn:.6f}")
print(__name__)
print(__file__)
import os
print(os.path.realpath(__file__))
x=open(__file__+'.txt','w')
x.write('nikhil')
x.write('nikhil')
# print(x.readline())
x.close()
x=open(__file__+'.txt','r')
# a=x.readline()
# print(a)
print(x.readlines())
# nodemon -x python aapractice.py
