'''
Use two pointers, i for the track of val and j for traversing the list,
if j is not equal to val then replace it with the i.

The idea is to replace the non-term with the val term so that the val term ends up last
'''

nums = [3,2,2,3]
val = 2

i = 0
for j in range(len(nums)):
    if nums[j] != val:
        nums[j], nums[i] = nums[i], nums[j]
        i+=1
print(i)