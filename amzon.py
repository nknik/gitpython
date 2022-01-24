class findxx(object):
    def __init__(self, a, b) -> None:
        super().__init__()
        self.a = a
        self.b = b
        # print(self.findx())

    def findx(self):
        # print(self.a,self.b)
        nk=[]
        for i in range(len(self.a)):
            # print("start")
            for j in range(len(self.a)):
                if i != j :
                    # print(self.a[i],self.a[j])
                    nk.append([abs(self.b-(self.a[i]+self.a[j])),self.a[i],self.a[j]])
        # aa=list(nk.values())
        aa=nk
        nk.sort(key=lambda a:a[0])
        # print(aa)   
        return nk[0][1],nk[0][2] 


if __name__ == "__main__":
    nk = findxx([10,22,28,29,30,40],54)
    print(nk.findx())
    nk = findxx([1, 3, 4, 7, 10],15)
    print(nk.findx())
