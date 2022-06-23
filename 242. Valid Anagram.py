# Problem Link https://leetcode.com/problems/valid-anagram/

def is_anagram(s, t):
    return sorted(s) == sorted(t)


print(is_anagram('rat', 'car'))
