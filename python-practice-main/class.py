class cars :
    def __init__(self,name,prise,tax):
        self.name=name
        self.prise=prise
        self.tax=tax
        # print(f"{name}  started  {prise}")
    # @classmethod
    def plus(self,*a):
        """
        docstring
        """
        print(f"{self.prise+self.tax} ----")
        print(f"{a[0]+a[1]} {a} ----")
a=cars("i20",200,300)
a.plus(10,20,30,40)

    