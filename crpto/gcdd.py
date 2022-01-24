from prettytable import PrettyTable
x = PrettyTable(hrules=1, title="nks GCD")
x.field_names = ["{a} ={a//b} * {b} + {a%b} "]
def gcd(a,b):
    pass
    b=abs(b)
    while(b>0):
        # print(f"{a} ={a//b} * {b} + {a%b} ")
        global x
        m=[f"{a} ={a//b} * {b} + {a%b}"]
        x.add_row(m)
        c=b
        b=a%b
        a=c
    # print("GCD IS =>",a)
    x.add_row([f"GCD IS =>{a}"])
    print(x)
    return a
print(gcd(8564,3246))               