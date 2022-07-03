# Problem Link https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
import collections


def can_be_equal(target, arr):
    return collections.Counter(target) == collections.Counter(arr)


print(can_be_equal([7], [7]))



