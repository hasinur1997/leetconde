# Problem Lik https://leetcode.com/problems/string-to-integer-atoi/

def atoi(s):
    num = 0
    s = s.strip()
    n = len(s)

    # Iterate till length of the string
    for i in s:
        # Subtract 48 from the current digit
        num = num * 10 + (ord(i) - 48)

    return num

print(atoi("-123"))
