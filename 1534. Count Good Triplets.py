# Problem Link https://leetcode.com/problems/count-good-triplets/

def count_good_triplets(arr, a, b, c):
    count = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1

    return count

print(count_good_triplets([3,0,1,1,9,7], 7, 2, 3))
