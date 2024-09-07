'''
Use two pointer, one for keeping track of the duplicates and one for unique value, 
as soon as you find unique value, change the i term to the j unique term.
'''


nums = [1,1,2]

i = 1
for j in range(1, len(nums)):
    if nums[j] != nums[i-1]:
        nums[i] = nums[j]
        i+=1
print(i)
