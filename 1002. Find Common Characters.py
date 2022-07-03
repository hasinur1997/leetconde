# Problem Link https://leetcode.com/problems/find-common-characters/

def common_chars(words):
    characters = []

    for i in words[0]:
        if all(i in x for x in words):
            for j in range(len(words)):
                words[j] = words[j].replace(i, "", 1)
            characters.append(i)

    return characters


print(common_chars(["bella","label","roller"]))

