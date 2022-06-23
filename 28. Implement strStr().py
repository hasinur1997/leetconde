# Problem Link https://leetcode.com/problems/implement-strstr/

def str_str(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

print(str_str('aaaaa', 'bba'))
