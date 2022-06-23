# Problem Link https://leetcode.com/problems/reverse-prefix-of-word/

def reverse_prefix(word, ch):

    if ch not in word:
        return word

    index = word.index(ch) + 1

    first = word[:index]
    second = word[index:]

    return first[::-1] + second


print(reverse_prefix("abcd", "z"))
