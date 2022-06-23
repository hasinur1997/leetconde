# Problem Link https://leetcode.com/problems/plus-one/

def plus_one(digits):
    number = int(''.join([str(item) for item in digits])) + 1
    number = str(number)

    return list(number)



print(plus_one([1,2,3]))
