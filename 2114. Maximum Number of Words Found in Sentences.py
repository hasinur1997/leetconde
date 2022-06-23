# Problem Link https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

def most_word_found(sentence):
    counts = []
    for st in sentence:
        words = st.split(' ')
        counts.append(len(words))
    return max(counts)


print(most_word_found(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))


