# Problem link https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def max_profit(prices):
    profits = []
    for num in range(len(prices)-1):
        profit = prices[num + 1] - prices[num]
        if profit > 0:
            profits.append(profit)

    return sum(profits)

max_profit([7,1,5,3,6,4])