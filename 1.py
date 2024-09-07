'''
traverse the array and subtract target - num, if the
difference is in the hash return the current index and the hash index else
create a hash of current num and index
'''

nums = [2,7,11,15]
target = 9

hash = {}
for i, num in enumerate(nums):
    if target - num in hash:
        print([i,hash[target-num]])
    hash[num] = i

