# Problem Link https://leetcode.com/problems/build-array-from-permutation/

def build_array(nums):
    return [nums[nums[i]] for i in range(len(nums))]


print(build_array([5,0,1,2,3,4]))

