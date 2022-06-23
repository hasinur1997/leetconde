# Problem Link
def nearest_valid_point(x, y, points):
    distance = []
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            distance.append(abs(points[i][0] - x) + abs(points[i][1] - y))
        else:
            distance.append(float('inf'))

    min_distance = min(distance)

    if min_distance == float('inf'):
        return -1

    return distance.index(min_distance)




print(nearest_valid_point(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))