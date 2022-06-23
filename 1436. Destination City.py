# Problem Link https://leetcode.com/problems/destination-city/

def dest_city(paths):

    if not paths:
        return False

    dest = []

    for path in paths:
        dest.append(path[0])

    for path in paths:
        if path[1] not in dest:
            return path[1]


print(dest_city(None))
