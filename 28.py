'''
set i to 0 and j to length of needle, now slice the haystack from i:j if the sliced portion is equal to the needle then return i,
if not then increment i and j by 1. also if j exceeds haystack return -1 meaning not found. 
'''

haystack = "sadbutsad"
needle = "sad"

i=0
j=len(needle)
while True:
    if j > len(haystack):
        print(-1)
        break
    if haystack[i:j] == needle:
        print(i)
        break
    i+=1
    j+=1