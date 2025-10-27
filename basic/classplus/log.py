def is_consecutive(nums):
    if len(nums) < 2:
        return False

    nums_sorted = sorted(nums)

    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i+1] - nums_sorted[i] != 1:
            return False

    return True


nums1 = [3, 2, 4, 1, 5]
print(is_consecutive(nums1)) 

nums2 = [1,10, 8, 6, 7, 9, 11, 12]
print(is_consecutive(nums2)) 
