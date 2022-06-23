# Problem Link https://leetcode.com/problems/find-common-characters/

def common_chars(words):
    characters = []
    string = ''.join(words)

    for ch in words[0]:
        checker = []
        for word in words[1:]:
            if ch in word:
                checker.append(True)
            else:
                checker.append(False)
        matched = all(e == True for e in checker)

        if matched:
            characters.append(ch)

    return characters


print(common_chars(["bella","label","roller"]))


