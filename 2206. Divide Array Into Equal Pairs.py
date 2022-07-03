# Problem Link https://leetcode.com/problems/divide-array-into-equal-pairs/
import collections

def divide_array(nums):
    return all(count % 2 == 0 for count in collections.Counter(nums).values())


print(divide_array([1,2,3,4]))


