# Problem Link https://leetcode.com/problems/reverse-string/

def reverse_string(s):
    rs = s[::-1]
    for index, char in enumerate(rs):
        s[index] = char

    return s


print(reverse_string(["h","e","l","l","o"]))
