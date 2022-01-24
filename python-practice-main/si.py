while 1:
    if 'q'== input("enter q to exit"):
        break
    else:
        p=float(input("principle"))
        n=float(input("year"))
        r=float(input("rate"))
        print("si",(p*n*r)/100,"si+p=",(p*n*r)/100+p)
        print("ci",(p*(1+r/100)**n)-p,"ci+p",(p*(1+r/100)**n))