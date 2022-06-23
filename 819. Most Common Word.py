# Problem Link https://leetcode.com/problems/most-common-word/
import string

def most_common_word(paragraph, banned):
    count_common_word = {}
    paragraph = paragraph.lower()

    for character in string.punctuation:
        paragraph = paragraph.replace(character, ' ')

    paragraph = paragraph.split(" ")
    print(paragraph)
    for word in paragraph:
        if word != ' '  and word not in banned:
            count_common_word[word] = paragraph.count(word)
    print(count_common_word)
    return max(count_common_word, key=lambda x: count_common_word[x])


print(most_common_word("Bob. hIt, baLl", ["bob", "hit"]))

"""
    "Bob. hIt, baLl"
["bob", "hit"]
"""