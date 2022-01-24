class City:
    def __init__(self, pincode, name, poppulation, area):
        self.pincode = pincode
        self.name = name
        self.poppulation = poppulation
        self.area = area


class District:
    def __init__(self, name, city):
        self.name = name
        self.city = city


if __name__ == "__main__":
    pass
    ppp = []
    n = []
    maxx = 99999999
    for i in range(int(input())):
        pincode = int(input())
        name = input()
        pop = int(input())
        area = int(input())
        n.append(pop)
        ppp.append(City(pincode, name, pop, area))
        if maxx > pincode:
            maxx = pincode
            nik = ppp[i]
    print(nik.pincode, nik.name, nik.poppulation, nik.area, sep="\n")
    n.sort()
    if n != []:
        print(*n, sep="\n")
    else:
        print("not found wali line tak")


# awk 'BEGIN{FS="|";OFS=",";count=0}{
#     if($3>15) && [[$2==*"Tata"*]]{
#         count=count+1;
#         print $1" "," "$2" "," "$3" "," "$4" ";
#     }
# }END{
#     if(count==0){
#         print "No wali line found";
#     }
# }'
