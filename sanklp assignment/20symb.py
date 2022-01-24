
"""Q.20 Write a python program to remove special symbols/functions from string."""

b = "abjaakjnckj27hwd2882hh3ud9hw3h39&&&&&&&%$#@!"
bb = list(filter(lambda a: a.isalnum(), b))
print(b, "-orignal string")
print("".join(bb))

""""
===================================OUTPUT============================
abjaakjnckj27hwd2882hh3ud9hw3h39&&&&&&&%$#@! -orignal string
abjaakjnckj27hwd2882hh3ud9hw3h39
===================================OUTPUT============================
"""