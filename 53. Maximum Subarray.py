# Problem link https://leetcode.com/problems/maximum-subarray/
def max_sub_array(nums):
    current_sum = 0
    max_sum = nums[0]

    for i in nums:
        if current_sum < 0:
            current_sum = 0

        current_sum += i
        max_sum = max(current_sum, max_sum)

    return max_sum


print(max_sub_array([5,4,-1,7,8]))

