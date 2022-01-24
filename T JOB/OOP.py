class Nikhil(object):
    name = "nikhil"

    def __init__(self) -> None:
        super().__init__()
        self.sirname="chalikwar"

    def nk(self) -> "nkkkk":
        print("class nIKHIL METHOD NK")

    @property
    def sete(self):
        return self.sirname
    @sete.setter
    def sete(self, n):
        self.sirname = n

    @sete.getter
    def sete(self):
        return self.sirname


    @classmethod
    def nkk(cls, n):
        cls.name = n

    @staticmethod
    def putter():
        print("staticmethod")

    def __str__(self):
        return self.__class__.name



class nk(Nikhil):
    def __init__(self) -> None:
        super().__init__()
        self.college="mgm"
        self.nn()
    def nn(self):
        super().nk()   
        print("class nk nn method")  
nk = nk()
print(repr(nk))
print(nk.sete)
nk.sete='chalikwaar'
# print(nk.sete)
# print(nk.sirname)
# print(dir(nk.nk))
# codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
# codeObejct = compile(codeInString, 'sumstring', 'exec')

# exec(codeObejct)
# import sys
# # nk=(1,2,3,4,5)
# nk={1,2,3,4,5,6}
# n=open("nk.txt","w")
# print(*nk,sep="\n",file=n,flush=True)
# nk={1:22}
# nk=**nk , nk.get('2',44)
# print(nk.get('2',44))
# h=5
# print(2**(h+1)-1)
# print(13|6)
# print(0|0)
print(Nikhil.Objects.all())