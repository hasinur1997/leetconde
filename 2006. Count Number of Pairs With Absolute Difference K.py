# Problem Link https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

def count_difference(nums, k):
    n = len(nums)
    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(nums[i] - nums[j]) == k:
                counter += 1

    return counter


print(count_difference([3,2,1,5,4], 2))
