# Problem Link https://leetcode.com/problems/largest-perimeter-triangle/

def largest_perimeter(nums):
    nums.sort(reverse=True)
    for a, b, c in zip(nums, nums[1:], nums[2:]):
        if b + c > a:
            return a + b + c

    return 0


print(largest_perimeter([1,2,1]))