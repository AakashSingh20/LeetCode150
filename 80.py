'''
Approach 1:
hashmap, keep a track of the elements and there count as soon as it reaches count = 3, pop it.

Approach 2:
two pointers, keep j pointer to traverse the array and i pointer to keep track of duplicates,
check if j = i-2, if yes then do nothing i++ j++, if j!= i-2 then replace i element with j and increament i.
'''



nums = [0,0,1,1,1,1,2,3,3]

# hash = {}
# i = 0

# while True:
#     if i == len(nums):
#         break
#     hash[nums[i]] = hash.get(nums[i],0) + 1
#     if hash.get(nums[i],0) and hash.get(nums[i]) > 2:
#         nums.pop(i)
#         continue
#     i+=1

# print(nums, len(nums))


i=0
for j in range(len(nums)):
    if i==0 or i==1 or nums[j] != nums[i-2]:
        nums[i] = nums[j]
        i+=1
print(i)