

# print(alpha.index('a')+1)
# print(alpha[0])


def printf(nk):
    print(f"{nk[0]} {nk[1]} {nk[2]} {nk[3]} {nk[4]}")


def find_c(m, d, n):
    pass
    return m**d % n


def find_m(m, d, n):
    pass
    return m**d % n


def find_d(e, fi):
    table = []
    table.append([1, 1, 0, fi, 1])
    table.append([2, 0, 1, e, fi//e])
    d = fi-(e*(fi//e))
    while table[-1][3] != 1:
        pass
        sr = table[-1][0]+1
        a = table[-2][1]-table[-1][1]*table[-1][-1]
        b = table[-2][2]-table[-1][2]*table[-1][-1]
        dd = table[-2][3]-table[-1][3]*table[-1][-1]
        table.append([sr, a, b, dd])
        # print(f"{table[-2][3]}//{table[-1][3]}")
        k = table[-2][3]//table[-1][3]
        table[-1].append(k)
        # print(sr, a, b, dd, k,end="\n")
        # table.append([sr, a, b, dd, k])
    pass
    for i in table:
        # print(i,end='\n')
        printf(i)
        pass
    print(b, end='<=d comes\n')
    final = b % fi
    if b > fi:
        final = b % fi
        print()
    if b < 0:
        final = b+fi
        print()
    print(final, end='hhh')
    return final


if __name__ == "__main__":
    pass
    p = 73
    q = 151
    n = p*q
    fi = (p-1)*(q-1)
    e = 11
    d = find_d(e, fi)
    while True:
        ccc = int(
            input("enter 1 find c\nenter 2 find m\nenter 3 string\nenter 4 for exit"))
        if ccc == 1:
            m = int(input("enter m"))
            c = find_c(m, e, n)
            print(
                f"n is {n}\np is {p}\ne is {e}\nfinal fi is {fi}\nfinal d is {find_d(e,fi)} and c is {c}")
        elif ccc == 2:
            c = int(input("enter c"))
            m = find_m(c, d, n)
            print(
                f"n is {n}\np is {p}\ne is {e}\nfinal fi is {fi}\nfinal d is {find_d(e,fi)} and M is {m}")
        elif ccc == 3:
            t ='who you are' #input("enter string")
            tt = ''
            m = find_m(c, d, n)
            print(
                f"n is {n}\np is {p}\ne is {e}\nfinal fi is {fi}\nfinal d is {find_d(e,fi)} and M is {m}")
        else:
            break

    m = find_m(c, d, n)
    print(f"final d is {find_d(e,fi)} and c is {m}")
    # print(f"final d is {find_d(480,7)}")
