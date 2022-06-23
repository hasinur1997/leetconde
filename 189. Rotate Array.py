# Problem Link https://leetcode.com/problems/rotate-array/

def rotate(nums, k):
    for i in range(k):
        m = nums.pop()
        nums.insert(0, m)

    return nums

print(rotate([1, 2], 3))
