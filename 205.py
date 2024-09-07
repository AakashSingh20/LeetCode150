'''
create two hashmaps, one for deriving s->t, and on for deriving t->s, and check if the letter is already present,
if the mapping of the letter is same in both the maps than its True else False. 
'''


s = "egg"
t = "add"

hash1 = {}
hash2 = {}

for i in range(len(s)):
    if s[i] in hash1 and hash1[s[i]] != t[i]:
        print(False)
    if t[i] in hash2 and hash2[t[i]] != s[i]:
        print(False)

    hash1[s[i]] = t[i]
    hash2[t[i]] = s[i]
print(True)