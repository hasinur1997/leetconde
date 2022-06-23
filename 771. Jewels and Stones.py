# Problem link :- https://leetcode.com/problems/jewels-and-stones/

def count_characters(char, strs):
    counter = 0
    for i in strs:
        if i in char:
            counter += 1
    return counter


print(count_characters('aA', 'aAAbbb'))
