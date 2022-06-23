# Problem Link https://leetcode.com/problems/add-binary/

def add_binary(a, b):
    sum = bin(int(a, 2) + int(b, 2))
    return sum[2:]


print(add_binary('11', '11'))

