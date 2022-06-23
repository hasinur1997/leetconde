# Problem Link https://leetcode.com/problems/single-number/

def single_number(nums):
    count_numbers = {}

    for num in nums:
        if num in count_numbers:
            count_numbers[num] += 1
        else:
            count_numbers[num] = 1

    for i in count_numbers:
        if count_numbers[i] == 1:
            return i


print(single_number([2,2,1]))


# numbers = [4,1,2,1,2]
#
# print(numbers[1:])
