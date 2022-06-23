# Problem Link https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kids_with_candies(candies, extraCandies):
    results = []

    for i in range(len(candies)):
        if candies[i] + extraCandies >= max(candies):
            results.append(True)
        else:
            results.append(False)

    return results


print(kids_with_candies([4,2,1,1,2], 1))
