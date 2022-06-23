def replace_elements(arr):
    array_copy = arr[:len(arr)]
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1
        else:
            arr[i] = max(array_copy[i+1:])

    return arr

print(replace_elements([17,18,5,4,6,1]))

print(max([5, 7]))
