# Problem Link https://leetcode.com/problems/monotonic-array/

def is_monotonic(nums):
    j = 1
    for i in range(len(nums)):
        if (i <= j and nums[i] <= nums[j]) or (i <= j and nums[i] >= nums[j]):
            return True
        j += 1

    return True


print(is_monotonic([6,5,4,4]))


test = [1, 2, 3, 4, 5]


