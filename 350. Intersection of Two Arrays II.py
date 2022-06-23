# Problem Link https://leetcode.com/problems/intersection-of-two-arrays-ii/

def intersect(nums1, nums2):
    common_values = []

    for i in nums1:
        if i in nums2:
            common_values.append(i)
            nums2.remove(i)

    return common_values

print(intersect([3,1,2], [1,1]))


# [1,1]