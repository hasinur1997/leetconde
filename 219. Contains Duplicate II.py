# Problem link https://leetcode.com/problems/contains-duplicate-ii/

def contains_duplicate(nums, k):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True

    return False

print(contains_duplicate([1,0,1,1], 1))