# Problem Link https://leetcode.com/problems/integer-to-roman/
"""
1000 - m
900 - cm
500 - d
400 - cd
100 - c
90 - xc
50 - l
40 - xl
10 - x
9 - ix
5 - v
4 - iv
1 - i

"""


def int_to_roman(num):
    xm = {
        "1000": "m",
        "900": "cm",
        "500": "d",
        "400": "cd",
        "100": "c",
        "90": "xc",
        "50": "l",
        "40": "xl",
        "10": "x",
        "9": "ix",
        "5": "v",
        "4": "iv",
        "1": "i"
    }
    roman = ''

    while num != 0:
        for i in xm:
            if num >= int(i):
                roman += xm[i]
                num -= int(i)
                break
    return roman.upper()

print(int_to_roman(1994))
