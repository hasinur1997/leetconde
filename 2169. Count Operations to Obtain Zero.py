# Problem Link https://leetcode.com/problems/count-operations-to-obtain-zero

def count_operations(num1, num2):
    counter = 0

    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

        counter += 1

    return counter


print(count_operations(2, 3))
