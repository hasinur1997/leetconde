# Problem Link https://leetcode.com/problems/valid-palindrome/
def is_palindrome(s):
    new_s = ''

    for ch in s:
        if ch.isalnum():
            print(ch)
            new_s += ch

    return new_s.lower() == new_s[::-1].lower()


print(is_palindrome("0P"))

