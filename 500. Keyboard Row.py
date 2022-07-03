# Problem Link https://leetcode.com/problems/keyboard-row/

def find_words(words):

    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    results = []

    for word in words:
        if all(ch in row1 for ch in word.lower()) or all(ch in row2 for ch in word.lower()) or all(ch in row3 for ch in word.lower()):
           results.append(word)

    return results


print(find_words(["omk"]))
