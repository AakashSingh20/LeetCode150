'''
First combine the two arrays by replacing zeros with the numbers, 
then apply merge sort to the list and save the result in an another list, 
then replace the values in the original list.

complexity = O(m+n)log(m+n)
'''

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

j=0
for i in range(m, len(nums1)):
    if nums1[i] == 0:
        nums1[i] = nums2[j]
        j+=1

def reduce(arr = nums1):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2

    l_half = arr[:mid]
    r_half = arr[mid:]

    l_half = reduce(l_half)
    r_half = reduce(r_half)

    return merge_sort(l_half, r_half)

def merge_sort(left , right):
    new=[]
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else:
             new.append(right[j])
             j+=1
        
    new.extend(left[i:])
    new.extend(right[j:])
    return new

sorted = reduce(nums1)
for i in range(len(sorted)):
    nums1[i] = sorted[i]
print("final",nums1)

