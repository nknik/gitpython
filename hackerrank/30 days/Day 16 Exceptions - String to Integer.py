# Input Format

# A single string, .

# Constraints

# , where  is the length of string .
#  is composed of either lowercase letters () or decimal digits ().
# Output Format

# Print the parsed integer value of , or Bad String if  cannot be converted to an integer.

# Sample Input 0

# 3
# Sample Output 0

# 3
# Sample Input 1

# za
# Sample Output 1

# Bad String
#!/bin/python3

import sys


try:
    print(int(input().strip()))
except ValueError:
    print("Bad String")
