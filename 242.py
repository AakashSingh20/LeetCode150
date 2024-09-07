'''
create a hash map for keeping the counts of the occurences, then traverse the t string and if any letter is not
found in the map then return false, else decrement by one. in the end check if the hash map has all zeros.
'''

s = "a"
t = "ab"

hash = {}

for i in range(len(s)):
    if s[i] not in hash:
        hash[s[i]] = 1

    else:
        hash[s[i]] += 1


for i in range(len(s)):
    if t[i] in hash and hash[t[i]] > 0:
        hash[t[i]] -= 1
    else:
        print(False)
    
print(all(count == 0 for count in hash.values()))


