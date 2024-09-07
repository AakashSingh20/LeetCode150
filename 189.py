'''
reverse the array, then reverse the first k term then reverse the rest terms,
also mod k cause sometimes k is larger than the length of nums.
'''


nums = [1,2,3,4,5,6,7]
k = 3

# nums[:] = nums[::-1]
k = k%len(nums)
nums.reverse()
nums[:k] = nums[:k][::-1]
nums[k:] = nums[k:][::-1]
print(nums)