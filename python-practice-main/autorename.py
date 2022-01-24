import os
import sys
while(1):
    name=input("enter folder name->")
    #name='Restored'
    new=f"{name}_Renamed"
    os.mkdir(new)
    for file in os.listdir(name):
        os.rename(f"{name}/{file}", f"{new}/{file}.jpg")
        #print(file)
    if(input("enter e to exit").lower=='e'):
        sys.exit(1)