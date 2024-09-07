'''
Use hashmap, mapping and comparing to find the largest count is done in one single loop, 
you can also use two loops one for mapping and another to find the largest count.
'''

nums = [3,2,3]
count = {}
val = counts = 0
for i in range(len(nums)):
    count[nums[i]] = 1 + count.get(nums[i],0)
    if count[nums[i]] > counts:
        counts = count[nums[i]]
        val = nums[i]
print(val)