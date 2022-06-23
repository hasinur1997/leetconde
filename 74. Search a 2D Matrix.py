# Problem Link https://leetcode.com/problems/search-a-2d-matrix/

def search_matrix(matrix, target):
    for i in matrix:
        if is_exist(i, target):
            return True
    return False


def is_exist(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high-low) // 2

        if array[mid] == item:
            return True

        if array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return False


# print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


def test(matrix, target):
    for i in matrix:
        if target in i:
            return True
    return False


print(test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))