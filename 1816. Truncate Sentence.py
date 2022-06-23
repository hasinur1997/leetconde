# Problem Link https://leetcode.com/problems/truncate-sentence/

def truncate_sentence(s, k):
    return ' '.join(s.split(' ')[0:k])

print(truncate_sentence('Hello how are you Contestant', 4))
