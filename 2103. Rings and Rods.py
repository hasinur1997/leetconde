# Problem Link https://leetcode.com/problems/rings-and-rods/

def count_points(rings):
    counted = []

    for i in range(10):
        r = 'R' + str(i)
        g = 'G' + str(i)
        b = 'B' + str(i)

        if r in rings and g in rings and b in rings and i not in counted:
            counted.append(i)

    return len(counted)


print(count_points('G4'))

