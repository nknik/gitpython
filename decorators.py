def nk(a):
    print("start")

    def nik(aa):
        return a(aa)


    print("end")
    return nik


@nk
def sq(a):
    # print(a)
    # return a
    return a ** 2


print(sq(2))
print(*list(range(8)),sep="\n",end=" ")