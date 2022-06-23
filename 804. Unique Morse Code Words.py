# Problem link https://leetcode.com/problems/unique-morse-code-words/

def unique_morse(words):
    morse = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }

    morse_encoded_words = []
    for word in words:
        transform = []
        for char in word:
            if char in morse:
                transform.append(morse[char])
        morse_encoded_words.append(''.join(transform))

    return len(set(morse_encoded_words))


# print(unique_morse(["gin","zen","gig","msg"]))
