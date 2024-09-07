'''
first map out all the letters in the magazine in the hashmap with the count,
then traverse the ransom note and if the letter is available in the hash map then decrement the count,
when the count of any letter hits zero it means that letter is not available and the note is incomplete.
'''

ransomNote = "a"
magazine = "b"

hash = {}

for i in range(len(magazine)):
    if magazine[i] not in hash:
        hash[magazine[i]] = 1
    else:
        hash[magazine[i]] += 1
print(hash)

for i in range(len(ransomNote)):
    if hash.get(ransomNote[i],0) > 0:
        hash[ransomNote[i]] -= 1
    else:
        print(False)
print(True)