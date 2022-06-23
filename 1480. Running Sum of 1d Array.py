# Problem Link https://leetcode.com/problems/running-sum-of-1d-array/

def running_sum(nums):
    ans = []

    for i in range(len(nums)):
        ans.append(sum(nums[:i+1]))

    return ans


print(running_sum([1,2,3,4]))


