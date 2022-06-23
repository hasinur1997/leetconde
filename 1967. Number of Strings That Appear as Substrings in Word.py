# Problem Link https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

def num_of_string(patterns, word: str) -> int:
    counter = 0
    for pattern in patterns:
        if pattern in word:
            counter += 1

    return counter

print(num_of_string(["a","b","c"], "aaaaabbbbb"))