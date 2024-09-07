'''
create a hashmap of all the brackets pair, and then initialize a stack, traverse the string using i
and check if i-1 is a pair of i, if yes then pop, if no then push. 
'''


s = "()[]{}"

arr=[]

map = { ')' : '(', ']' : '[', '}' : '{' }

for i in range(len(s)):
    if arr and (s[i] in map) and arr[-1] == map[s[i]]:
        arr.pop()
    else:
        arr.append(s[i])

if len(arr) == 0:
    print(True)
else:
    print(False)