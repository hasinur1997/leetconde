# Problem Link https://leetcode.com/problems/merge-strings-alternately/

def merge_alternately(word1, word2):
    new_str = ''
    lare_str = word1

    if len(word2) > len(word1):
        lare_str = word2

    for i in range(len(lare_str)):
        if i < len(word1) and i < len(word2):
            new_str += word1[i] + word2[i]
        else:
            new_str += lare_str[i:]
            break
    return new_str


print(merge_alternately('ab', 'pqrs'))

