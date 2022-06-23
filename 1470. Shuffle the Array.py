# Problem Link https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    x = nums[:n]
    y = nums[n:]
    ans = []

    for i in range(n):
        ans.append(x[i])
        ans.append(y[i])

    return ans

print(shuffle([1,2,3,4,4,3,2,1], 4))
