# Problem Link https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

def count_pairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums), 1):

            if nums[i] == nums[j] and i * j % 2 == 0:
                count += 1
    return count


print(count_pairs([1,2,3,4], 1))
