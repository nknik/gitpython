# STDIN   Function
# -----   --------
# 3       __elements[] size N = 3
# 1 2 5   __elements = [1, 2, 5]
# Sample Output

# 4
# find largest difference
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    def computeDifference(self):
        self.maximumDifference=max([i-j for i in self.__elements for j in self.__elements])

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)