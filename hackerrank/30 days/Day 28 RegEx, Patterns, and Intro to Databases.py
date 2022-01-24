# Sample Input

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com
# Sample Output

# julia
# julia
# riya
# samantha
# tanya
#!/bin/python3

import re


nk = []
if __name__ == "__main__":
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search(".+@gmail\.com$", emailID):
            nk.append(firstName)

nk.sort()
for name in nk:
    print(name)
