import os
import re
import textwrap
import datetime as d


class notes:
    user = 'nikhil@ubantu'
    cwd = os.getcwd()
    ts = 0

    def __init__(self):
        notes.ts = notes.timestamp()
        self.chck()
        self.filename = input("enter file name=>")
        self.file = open(self.filename+'.txt', 'w')
        self.file.write("loading script...... \n")
        while(input("1 for add 0 for exit") != '0'):
            self.header()
            self.question()
        self.file.write(f"{'$'*60} \n")
        self.file.write(f" automated script ended at {notes.timestamp()}...... \n")
        self.file.write(f"{'$'*60} \n")
        self.file.close()

    def question(self):
        pass
        self.a = ''
        self.b = ''
        while (1):
            self.temp = input("enter query 00 to end")
            if self.temp == '00':
                break
            self.a += self.temp

        self.file.write("\nquery-\n")
        self.file.write(textwrap.fill(self.a, width=60))
        self.file.write("\nsolution----------------\n")
        while (1):
            self.temp = input("enter query 00 to end")
            if self.temp == '00':
                break
            self.b += self.temp
        self.file.write(textwrap.fill(self.b, width=60))
        self.file.write("\n")

    def chck(self):
        print(notes.ts)

    def header(self):
        self.file.write("\n")
        self.file.write("#".center(60, '#'))
        self.file.write("\n")
        self.file.write(
            f'{notes.timestamp()}....user=Nikhil@ubantu'.center(60, '.'))
        self.file.write("\n")
        self.file.write(f'dir=> {notes.cwd}'.center(60, '.'))
        self.file.write("\n")
        self.file.write("#".center(60, '#'))
        self.file.write("\n")

    @staticmethod
    def timestamp():
        """timestamp()=>gives whole timestamp"""
        date = dict()
        date['timestamp'] = "Date=>"+str(d.datetime.now())[:10][-2:]+"-"+str(
            d.datetime.now())[:10][-5:-2]+str(d.datetime.now())[:4]+"  Time=>"
        if int(str(d.datetime.now())[10:13]) > 12:
            date['timestamp'] += "  " + \
                str(int(str(d.datetime.now())[10:13]) -
                    12)+' PM'+str(d.datetime.now())[13:19]
        elif int(str(d.datetime.now())[10:13]) == 12:
            date['timestamp'] += "  " + \
                str(int(str(d.datetime.now())[10:13])) + \
                ' PM'+str(d.datetime.now())[13:19]
        else:
            date['timestamp'] += "  " + \
                str(int(str(d.datetime.now())[10:13])) + \
                ' AM'+str(d.datetime.now())[13:19]
        return date['timestamp']


n = notes()
# print(n.ts)
print("nk")
