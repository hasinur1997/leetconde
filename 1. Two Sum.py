# Problem Link https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    indix = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                indix.append(i)
                indix.append(j)
    return indix


print(two_sum([3,2,4], 6))