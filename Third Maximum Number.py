# Prblem Link https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/

def third_max(nums):
    nums = list(set(nums))
    if len(nums) >= 3:
        nums.sort(reverse=True)
        return nums[2]

    return max(nums)

print(third_max([1,1, 2]))