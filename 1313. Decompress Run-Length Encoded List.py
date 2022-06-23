# Problem Link https://leetcode.com/problems/decompress-run-length-encoded-list/

def decompress_relist(nums):
    results = []
    for i in range(0, len(nums), 2):
        results += [nums[i+1]] * nums[i]

    return results


def threeSum(nums):
    triplets = []

    j = 1
    k = 2

    for i in range(len(nums) - 2):

        new_items = [nums[i], nums[j], nums[k]]

        if sum(new_items) == 0:
            triplets.append(new_items)
        j += 1
        k += 1
    return triplets


print(threeSum([-1,0,1,2,-1,-4]))
