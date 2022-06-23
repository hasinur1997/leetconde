# ["flower","flow","flight"]

# Get the first word
# Compare ech character to all word's character
# If a character match all the word sequence character then push it to the prefix character array
# Convert the character array to string
# return the prefix string
# strs = ["cir","car"]
# strs = ["flower","flow","flight"]
strs = ["abab","aba",""]
strs = [""]
first_word = strs[0]
prefix = []

for index, character in enumerate(first_word):
    checked = []
    is_matched = True
    for word in strs[1:]:
        if index >= len(word):
            is_matched = False
            break
        if character != word[index]:
            is_matched = False
            break

        if character == word[index]:
            checked.append(True)
        else:
            checked.append(False)

    if not is_matched:
        break

    if len(checked) > 0 and all(element == True for element in checked):
        prefix.append(character)
        print(character)


prefix = ''.join(prefix)
# print(prefix)