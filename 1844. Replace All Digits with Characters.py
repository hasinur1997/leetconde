# Problem Link https://leetcode.com/problems/replace-all-digits-with-characters/

def replace_digit(s):
    st = ''

    for index, ch in enumerate(s):
        if ch.isdigit():
            st += chr(ord(s[index-1]) + int(ch))
        else:
            st += ch
    return st


print(replace_digit('a1b2c3d4e'))
