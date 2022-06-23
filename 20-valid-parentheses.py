
def is_valid_parentheses(string):
    parentheses = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in string:
        if c in parentheses:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if c != parentheses[top]:
                return False

    return len(stack) == 0


print(is_valid_parentheses('(]'))