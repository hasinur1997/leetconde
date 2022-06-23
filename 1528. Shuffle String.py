# Problem Link https://leetcode.com/problems/shuffle-string/

def restore_string(s, indices):
    indices_length = len(indices)
    restore = [None] * indices_length

    for i in range(indices_length):
        restore[indices[i]] = s[i]
    return ''.join(restore)


print(restore_string('abc', [0,1,2]))
