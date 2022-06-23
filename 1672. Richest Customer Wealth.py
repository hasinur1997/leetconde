# Problem Link
def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        max_wealth = max(max_wealth, sum(customer))

    return max_wealth


print(maximum_wealth([[1,5],[7,3],[3,5]]))
