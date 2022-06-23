def sum_odd_sub_array(arr):
    summation = 0
    for i in range(1, len(arr) + 1, 2):
        j = 0
        while j <= len(arr) - i:
            summation += sum(arr[j:j + i])
            j += 1
    return summation


print(sum_odd_sub_array([1,4,2,5,3]))
