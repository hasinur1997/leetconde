# Problem Link https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def find_disappeared_numbers(nums):
    return list(set(range(1, len(nums) + 1)).difference(nums))


print(find_disappeared_numbers([1, 1]))

