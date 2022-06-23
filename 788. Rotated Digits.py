# Problem Link https://leetcode.com/problems/rotated-digits/

def is_good(num):
    goods = [2, 5, 6, 9]
    bad = [3, 4, 7]

    num = str(num)
    is_change = False
    for i in num:
        if int(i) in bad:
            return False
        if int(i) in goods:
            is_change = True

    return is_change

# is_good(857)

def rotated_digits(n):
    counter = 0
    good_numbers = [2, 5, 6, 9]

    for num in range(1, n+1):
        # print(is_good(num))
        if is_good(num):
            counter += 1
    return counter


print(rotated_digits(857))

