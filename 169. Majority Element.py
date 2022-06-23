# Problem Link https://leetcode.com/problems/majority-element/

def majority_element(nums):
    n = len(nums) / 2
    numbers = {}

    for num in nums:
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1

    for num in numbers:
        if numbers[num] > n:
            return num


print(majority_element([2,2,1,1,1,2,2]))

