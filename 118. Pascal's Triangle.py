# Problem Link https://leetcode.com/problems/pascals-triangle/
def generate(numRows):
    rows = []
    c = 1
    for i in range(1, numRows+1):
        item = []
        for j in range(1, i+1):
            rows.append(c)
            c = c * (i - j) // j
        rows.append(item)
    return rows


print(generate(10))
