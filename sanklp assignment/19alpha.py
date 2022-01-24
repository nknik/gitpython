"""Q.19 Write a python

program finds words with both alphabets and numbers from the string. """
b = "abjaakjnckj27hwd2882hh3ud9hw3h39"
aa = []
aaa = []
for i in b:
    if not i.isdigit():
        aa.append(i)
    else:
        aaa.append(i)
print(f"words->{aa}\n digit{aaa}")
"""
===================================OUTPUT===================================
words->['a', 'b', 'j', 'a', 'a', 'k', 'j', 'n', 'c', 'k', 'j', 'h', 'w', 'd', 'h', 'h', 'u', 'd', 'h', 'w', 'h']
 digit['2', '7', '2', '8', '8', '2', '3', '9', '3', '3', '9']
===================================OUTPUT===================================
"""