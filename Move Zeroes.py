def move_zeros(nums):
    j = 0
    for i in range(len(nums)):
       if nums[i] != 0:
           nums[j] = nums[i]
           j += 1

    for c in range(j, len(nums)):
        nums[c] = 0

    return nums


print(move_zeros([0,1,0,3,12]))
