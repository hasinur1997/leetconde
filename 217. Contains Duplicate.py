# Problem link https://leetcode.com/problems/contains-duplicate/
def contain_duplicate(nums):
    return len(nums) != len(set(nums))


print(contain_duplicate([1,1,1,3,3,4,3,2,4,2]))