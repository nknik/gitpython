class fuelst:
    def __init__(self):
        self.pump = {'A': False, 'B': False, 'C': False, 'D': False}
        self.pri = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        self.tank = 0.0
        self.pp = [1, 2, 3, 4]
        self.ppp = ['A', 'B', 'C', 'D']

    def startpump(self, n):
        self.pump[n] = True
        self.work()
        pass

    def fail(self, n):
        pass
        print(self.ppp)
        self.pump[n] = 'failed'
        nk = self.ppp.index(n)
        k = self.ppp.pop(nk)
        self.ppp.append(k)
        print(self.ppp)
        self.work()

    def work(self):
        self.pump = {'A': False, 'B': False, 'C': False, 'D': False}

        if self.tank >= 1:
            self.pump[self.ppp[0]] = True
        if self.tank >= 2:
            self.pump[self.ppp[1]] = True
        if self.tank >= 3:
            self.pump[self.ppp[2]] = True
        if self.tank < 4 and self.tank > 3:
            self.pump[self.ppp[3]] = True

        if self.tank == 4:
            for i in self.pump.keys():
                self.pump[i] = False
        self.Disaply()

    def Disaply(self):
        for i, j in self.pump.items():
            print(i, ' motor is on?->', j)


if __name__ == "__main__":
    print('nikhil')
    nk = fuelst()
    nk.tank = float(input('enter the current value of tank'))
    nk.work()
    while True:

        n = int(input(
            'enetr 1 for exit\n2 for fail \n3 display\n 4 for start failed motor \n 5 for restart'))
        if n == 1:
            break
        if n == 2:
            nk.fail((str(input('enetr failed motor'))).upper())
        if n == 3:
            nk.Disaply()
        if n == 4:
            nk.startpump((str(input('enetr failed motor'))).upper())
        if n == 5:
            nk.tank = float(input('enter the current value of tank'))


# Try the new cross-platform PowerShell https://aka.ms/pscore6

# PS C:\Users\Aarya> conda activate base
# PS C:\Users\Aarya> & C:/Users/Aarya/Anaconda3/python.exe c:/Users/Aarya/Desktop/fuel.py
# nikhil
# enter the current value of tank3.0
# A  motor is on?-> True
# B  motor is on?-> True
# C  motor is on?-> True
# D  motor is on?-> False
# enetr 1 for exit
# 2 for fail
# 3 display
#  4 for start failed motor
#  5 for restart2
# enetr failed motora
# ['A', 'B', 'C', 'D']
# ['B', 'C', 'D', 'A']
# A  motor is on?-> False
# B  motor is on?-> True
# C  motor is on?-> True
# D  motor is on?-> True
# enetr 1 for exit
# 2 for fail
# 3 display
#  4 for start failed motor
#  5 for restart1
# PS C:\Users\Aarya>
