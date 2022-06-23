def find_max_consecutive(nums):
    counter = 0
    max_ones = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            counter = 0
        else:
            counter += 1

        max_ones = max(counter, max_ones)

    return max_ones


print(find_max_consecutive([1,1,0,1,1,1]))
