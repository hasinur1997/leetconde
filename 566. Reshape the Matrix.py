# Problem Link https://leetcode.com/problems/reshape-the-matrix/

def reshape(mat, r, c):
    total_element = len(mat[0]) * len(mat)
    r_c = r * c
    if total_element != r_c:
        return mat

    new_mat = [item for sub in mat for item in sub]
    counter = 0
    new_array = []
    new_item = []
    for i in range(r*c):
        print(c)
        if len(new_item) == c:
            print(c)
            print(len(new_item))
        # print(new_mat[counter])
        new_item.append(new_mat[counter])
        # print(c)

        counter += 1
    return new_array


print(reshape([[1,2], [3,4]], 1, 4))