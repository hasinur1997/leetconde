# Problem Link https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

def find_the_distance_value(arr1, arr2, d):
    counter = 0
    distances = set()

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if abs(arr1[i] - arr2[j]) <= d and abs(arr2[j]) not in arr1:
                counter += 1

    return counter

print(find_the_distance_value([2,1,100,3],[-5,-2,10,-3,7],6))
