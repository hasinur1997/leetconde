# Problem Link https://leetcode.com/problems/climbing-stairs/

def climb_stairs(n):
    a = [0, 1, 2]

    if n > 2:
        for i in range(3, n+1):
            a.append(a[i-1] + a[i-2])

    return a[n]

print(climb_stairs())