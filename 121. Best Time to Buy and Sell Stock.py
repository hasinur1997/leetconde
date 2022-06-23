# Problem Link https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices):
    profit = 0
    min = prices[0]

    for i in range(1, len(prices)):
        if prices[i] > min:
            profit = max(profit, prices[i] - min)
        else:
            min = prices[i]

    return profit


print(max_profit([7,1,5,3,6,4]))