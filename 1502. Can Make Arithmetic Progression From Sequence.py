# Problem Link https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

def can_make_arithmatic_progression(arr):
    arr.sort()
    if len(arr) == 2:
        return

    for i in range(1, len(arr) - 1):
        if arr[i+1] - arr[i] != arr[i] - arr[i-1]:
            return False
    return True


print(can_make_arithmatic_progression([0,0,1]))

# print(0-0)