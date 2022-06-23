# Problem link https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

def count_odd(low, high):
    if low % 2 == 0 and high % 2 == 0:
        return (high - low) // 2

    return (high - low) // 2 + 1


print(count_odd(1, 11))

