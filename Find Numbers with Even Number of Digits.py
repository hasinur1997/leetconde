def find_numbers(nums):
    counter = 0
    for i in nums:
        digit = count_digit(i)

        if digit % 2 == 0:
            counter += 1

    return counter


def count_digit(number):
    count_digit = 0
    while number > 0:
        number = number // 10
        count_digit += 1

    return count_digit


print(find_numbers([12,345,2,6,7896]))
