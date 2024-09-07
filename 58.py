'''
traverse from the end , and find the first letter and store the index in i, then traverse from that i and increment the count until
the blank space occurs.
'''


s = "Hello World"
count = 0
i = len(s) - 1

while i>=0 and s[i] == " ":
    i-=1

while i>=0 and s[i] != " ":
    count +=1
    i-=1

print(count)