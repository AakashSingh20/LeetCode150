'''
keep a track of max reach, so first travese the array and check the reach by adding the nums[i] to i,
compare with the previous reach and keep the max reach, if the i pointer crosses the reach then return 
False
'''

nums = [3,2,1,0,4]

reach = 0

for i in range(len(nums)):
    if reach < i:
        print(False)
        break
    reach = max(reach, i + nums[i])

print(True, reach)