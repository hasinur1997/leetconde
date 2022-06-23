# Problem Link https://leetcode.com/problems/check-if-the-sentence-is-pangram/

def is_pangram(sentence):
    pangram = 'thequickbrownfoxjumpsoverthelazydog'
    count_pangram = []
    
    for char in pangram:
        if char in sentence:
            count_pangram.append(True)
        else:
            count_pangram.append(False)

    if len(count_pangram) > 0 and all(element == True for element in count_pangram):
        return True

    return False


print(is_pangram('thequickbrownfoxjumpsoverthe'))
