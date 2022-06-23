# Problem Link https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

def swap_string(s1, s2):
    if s1 == s2:
        return True

    a = []
    b = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            a.append(s1[i])
            b.append(s2[i])


    if len(a) == len(b) == 2:
        if a[0] == b[1] and b[0] == a[1]:
            return True

    return False

print(swap_string('kelb', 'kelb'))