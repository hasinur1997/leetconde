# Problem Link https://leetcode.com/problems/next-greater-element-i/

def next_greater_element(nums1, nums2):
    ans = []

    for i in nums1:
        index = nums2.index(i)
        for j in nums2[index+1:]:
            if j > i:
                ans.append(j)
                break
        else:
            ans.append(-1)

    return ans


print(next_greater_element([1,3,5,2,4], [6,5,4,3,2,1,7]))
