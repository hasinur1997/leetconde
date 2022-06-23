# Problem Link https://leetcode.com/problems/uncommon-words-from-two-sentences/

def uncommon_words_from_sentence(s1, s2):
    new_string = list(s1.split(" ") + s2.split(" "))
    uncommon = []

    for word in new_string:
       if new_string.count(word) < 2:
           uncommon.append(word)

    return uncommon


print(uncommon_words_from_sentence("apple apple", "banana"))
