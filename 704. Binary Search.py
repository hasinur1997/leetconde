# Problem Link https://leetcode.com/problems/binary-search/

def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(search([1,0,3,5,9,12], 1))
