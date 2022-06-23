# Problem Link https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

def array_string_equal(word1, word2):

    if ''.join(word1) == ''.join(word2):
        return True

    return False


print(array_string_equal(["a", "cb"], ["ab", "c"]))
