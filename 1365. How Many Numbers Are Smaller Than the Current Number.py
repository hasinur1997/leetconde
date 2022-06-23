# Problem Link:- https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def count_smaller_number(nums):
    count_numbers = []

    for i in nums:
        counter = 0
        for j in nums:
            if j < i:
                counter += 1
        count_numbers.append(counter)

    return count_numbers


print(count_smaller_number([7,7,7,7]))
