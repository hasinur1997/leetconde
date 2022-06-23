# Problem Link

def can_construct(ransomNote, magazine):
    counter = 0

    for ch in ransomNote:
        if ch in magazine:
            magazine = magazine.replace(ch, '', 1)
            counter += 1

    return len(ransomNote) == counter


print(can_construct('aa', 'ab'))
