nums = [1,2,3,1,2,3]
k = 2

hash = set()

l = 0

for i in range(len(nums)):
    if i - l > k:
        hash.remove(nums[l])
        l+=1

    if nums[i] in hash:
        print(True)
        break
    
    hash.add(nums[i])
print(False)