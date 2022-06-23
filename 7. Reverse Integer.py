# Problem Link https://leetcode.com/problems/reverse-integer/

def reverse(x):
    negative = False
    x = list(str(x))

    if x[0] == '-':
        negative = True
        x = x[1:]

    x = int(''.join(x[::-1]))

    if x < -2**31 or x > 2**31:
        return 0

    if negative:
        return -x

    return x

print(reverse(123))