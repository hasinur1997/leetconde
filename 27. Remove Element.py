# Problem Link https://leetcode.com/problems/remove-element/

def remove_element(nums, val):
    j = 0

    for i in range(len(nums)):
        if nums[i] == val:
            j += 1
            nums[j] = nums[i]

    return nums


print(remove_element([3,2,2,3], 3))
