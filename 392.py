'''
use two pointers, j for the s, i for the t. if i term equals to the j term then increment the j, keep on doing this until j reaches 
the size of s. in than case s exists in t, if the i esxeeds length of t that means not found.
'''

s = "abc"
t = "ahbgdc"

j = 0

for i in t:
    if j == len(s):
        print(True)
    if i == s[j]:
        j+=1

if j == len(s):
    print(True)
else:
    print(False)