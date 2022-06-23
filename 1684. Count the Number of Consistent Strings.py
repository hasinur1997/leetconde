# Problem link https://leetcode.com/problems/count-the-number-of-consistent-strings

def count_consistent_string(allowed, words):
    counter = 0
    for word in words:
        consistent_count = []

        for character in word:
            if character in allowed:
                consistent_count.append(True)
            else:
                consistent_count.append(False)

        if len(consistent_count) > 0 and all(element == True for element in consistent_count):
            counter += 1

    return counter


print(count_consistent_string('ab', ["ad","bd","aaab","baa","badab"]))
