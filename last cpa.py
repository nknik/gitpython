class Passenger:
    def __init__(self, pid, pname, sno, meal, clls):
        pass
        self.pid = pid
        self.pname = pname
        self.sno = sno
        self.meal = meal
        self.clls = clls
        bm = {}

    def __str__(self):
        return f"{self.pid},{self.pname} "


if __name__ == "__main__":
    pass
    passe = []
    for i in range(int(input())):
        pid = int(input())
        pname = input()
        sno = input()
        meal = input()
        clls = input()
        passe.append(Passenger(pid, pname, sno, meal, clls))
    eco = []
    eco[0] = input()
    eco[1] = input()
    biz = []
    biz[0] = input()
    biz[1] = input()
    sno = input()
    pid = 0
    pidd = 0
    for i in passe:
        if sno.lower() == i.sno.lower():
            sno = i.clls
        if i.clls.lower() == "economy" and i.meal.lower() == "yes":
            pid += 1
        elif i.clls.lower() == "economy" and i.meal.lower() == "no":
            pidd += 1
    if pid == 0:
        print("no passaenger in economy class")
    else:
        print("economy yes wali line", pid)
        print("economy no wali line", pidd)
    if sno == 0:
        print("passanger does not belongs to bizz class class")
    elif sno.lower() == "business":
        print(*biz, sep="\n")
    if sno.lower() == "economy":
        print(*eco, sep="\n")
