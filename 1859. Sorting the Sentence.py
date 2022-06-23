# Problem Link: https://leetcode.com/problems/sorting-the-sentence/

def sort_sentence(s):
    words = s.split(' ')
    new_sentence = ["0" for word in words]

    for word in words:
        new_sentence[int(word[-1]) - 1] = word[:-1]

    return ' '.join(new_sentence)


print(sort_sentence('lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1'))