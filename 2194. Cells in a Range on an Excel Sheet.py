# Problem Link https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

def get_cel_in_range(s):
    ans = []
    for r in range(ord(s[0]), ord(s[3]) + 1):
        for c in range(int(s[:1]), int(s[:4]) + 1):
            ans.append(chr(r) + str(c))
    return ans


print(get_cel_in_range('K1:L10'))
