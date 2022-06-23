# Problem Link https://leetcode.com/problems/transpose-matrix/

def tranpose(matrix):
    new_array = []
    for i in range(len(matrix[0])):
           new_items = []
           for j in range(len(matrix)):
               new_items.append(matrix[j][i])
           new_array.append(new_items)

    return new_array
print(tranpose([[1,2,3],[4,5,6]]))



"""
[
[1,2,3],
[4,5,6]
]

[1, 4],
[2, 5],
[3, 6]


[
    [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        
"""