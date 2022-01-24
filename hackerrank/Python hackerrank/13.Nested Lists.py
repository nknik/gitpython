marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print("\n".join([a for a, b in sorted(marksheet) if b == second_highest]))


if __name__ == "__main__":
    nk = []
    for _ in range(int(input())):
        nk.append([input(), float(input())])
    n = sorted(list(set([y for x, y in nk])))[-1]
    print("\n".join([x for x, y in nk if y == n]))
