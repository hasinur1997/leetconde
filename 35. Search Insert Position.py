# Problem Link
def search_insert(nums, target):
    index = binary_search(nums, target)

    if index >= 0:
        return index

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

print(binary_search([1,3,5,6], 13))
