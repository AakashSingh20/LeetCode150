'''
Use hashmap, if the i term is bigger than i+1 then add to the result otherwise if the i term is less than the i+1 then subtract i from i+1 and add 
to the result
'''
s = "III"
hash = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
result = 0
i = 0
j = len(s)

while i<j:

    if i<j-1 and hash[s[i]] < hash[s[i+1]]:
        result += hash[s[i+1]] - hash[s[i]]
        i+=2

    else:
        result += hash[s[i]]
        i+=1
print(result)