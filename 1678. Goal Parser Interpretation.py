# Problem link https://leetcode.com/problems/goal-parser-interpretation/

def interpret(s):
    if not s:
        return ''

    if '()' in s:
        s = s.replace('()', 'o')
    if '(al)' in s:
        s = s.replace('(al)', 'al')

    return s


print(interpret(None))
