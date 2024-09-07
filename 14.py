'''
Assume the first word in the array is prefix then traverse through the rest of the array and compare the word to the prefix,
if the word doesnt match, then remove one letter from the back until it does and then update the prefix, then check for the next word.
'''

strs = ["flower","flow","flight"]

if not strs:
    print ("")

prefix = strs[0]

for i in strs:
    while i[:len(prefix)] != prefix:
        prefix = prefix[:-1]

        if not prefix:
            print("")
print(prefix)