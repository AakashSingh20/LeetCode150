'''
filter the alpha num from the string and now just check with two pointers if they are same or not.
'''

s = "A man, a plan, a canal: Panama"

a = ""
for i in s:
    if i.isalnum():
        a+=i.lower()

left = 0
right = len(a)-1

while left < right:
    if a[left] != a[right]:
        print (False)
    else:
        left+=1
        right-=1
print (True)