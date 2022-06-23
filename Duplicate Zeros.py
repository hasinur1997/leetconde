def duplicate_zeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.insert(i+1, 0)
            i += 1
            arr.pop()

    return arr


print(duplicate_zeros([1,0,2,3,0,4,5,0]))

