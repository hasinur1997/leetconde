# Problem Link https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverse_words(s):
    words = s.split(' ')

    words = [word[::-1] for word in words]

    return ' '.join(words)

print(reverse_words('God Ding'))