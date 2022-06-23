# Problem Link https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

def count_negatives(grid):
    counter = 0

    for nums in grid:
        for n in nums:
            if n < 0:
                counter += 1

    return counter

print(count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
