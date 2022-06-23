def is_exists(arr):
    for i, n in enumerate(arr):
        if 2*n in arr:
            print(2*n)
            return True
    return False


print(is_exists([2,4,3,5,7,11]))
