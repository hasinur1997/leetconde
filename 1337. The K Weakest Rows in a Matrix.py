# Problem Link https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

def k_weakest_rows(mat, k):
    weakests = {}

    for i in range(len(mat)):
        weakests[i] = mat[i].count(1)

    weakests = list({k: v for k, v in sorted(weakests.items(), key=lambda item:item[1])}.keys())

    return weakests[:k]

print(k_weakest_rows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2))
