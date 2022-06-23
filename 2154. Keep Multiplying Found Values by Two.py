# Problem Link https://leetcode.com/problems/keep-multiplying-found-values-by-two/

def find_final_value(nums, original):

    while original in nums:
        original *= 2

    return original

print(find_final_value([2,7,9], 4))