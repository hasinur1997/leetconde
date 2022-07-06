# Problem Link https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

def min_add_to_make_valid(s):
    stack = []
    for ch in s:
        print(ch)
        if ch == "(":
            stack.append(ch)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(ch)
                print(stack)
    return len(stack)


print(min_add_to_make_valid('())'))


