# Problem Link https://leetcode.com/problems/rotate-image/

def rorate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix

print(rorate([[1,2,3],[4,5,6],[7,8,9]]))
