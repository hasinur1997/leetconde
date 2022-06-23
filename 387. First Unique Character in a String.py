# Problem Link https://leetcode.com/problems/first-unique-character-in-a-string/

def first_unique_char(s):
    memory = {}
    for index, ch in enumerate(s):
        if ch not in memory:
            memory[ch] = index
        else:
            memory[ch] = False

    for key, value in memory.items():
        if value is not False:
            return value

    return -1


print(first_unique_char("aab"))


