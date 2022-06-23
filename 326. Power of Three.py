# Problem Link https://leetcode.com/problems/power-of-three/

def is_power_of_three(n):
    if n <= 0:
        return False
    return n % 3 == 0


print(is_power_of_three(-1))