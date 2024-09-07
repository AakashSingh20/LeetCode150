'''
t = pattern!!

create two hashmaps, one for deriving s->t, and on for deriving t->s, and check if the letter is already present,
if the mapping of the letter is same in both the maps than its True else False. 
'''

pattern = "abba"
s = "dog cat cat dog"
s = s.split(" ")

hash1 = {}
hash2 = {}

for i in range(len(s)):
    if s[i] in hash1 and hash1[s[i]] != pattern[i]:
        print(False)
    if pattern[i] in hash2 and hash2[pattern[i]] != s[i]:
        print(False)

    hash1[s[i]] = pattern[i]
    hash2[pattern[i]] = s[i]
print(True)
