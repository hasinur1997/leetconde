# Problem Link https://leetcode.com/problems/check-if-it-is-a-straight-line/

def check_strait_line(coordinates):
    if not coordinates:
        return False

    x0 = coordinates[0][0]
    x1 = coordinates[1][0]

    y0 = coordinates[0][1]
    y1 = coordinates[1][1]
    dx = x1 - x0
    dy = y1 - y0

    for i in range(2,len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]

        if dy * (x-x0) != dx * (y-y0):
            return False

    return True


print(check_strait_line([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
