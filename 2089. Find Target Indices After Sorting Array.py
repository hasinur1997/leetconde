# Problem Link https://leetcode.com/problems/find-target-indices-after-sorting-array/

def target_indices(nums, target):
    if not nums:
        return []

    indices = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)

    return indices


print(target_indices([1,2,5,2,3], 5))