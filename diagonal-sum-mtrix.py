def diagonal_sum(mat):
    summation = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (i == j) or (i + j == len(mat) - 1):
                summation += mat[i][j]

    return summation