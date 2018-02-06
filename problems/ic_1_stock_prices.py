#
# Problem: Given an array representing stock prices at every sequential minute
# in a given day, find the greatest possible profit if we are able to buy and
# sell only once each.
#
# For example:
# Given stock prices: [10, 7, 5, 8, 11, 9]
# Greatest profit = 6 (buy at 5 and sell at 11)
#


def stock_prices_1_brute_force(stock_prices):
    """
    Solution: Brute force iterative solution compares each stock price with
    all subsequent stock prices.
    Complexity:
        Time: O(n^2)
        Space: O(1)
    """
    if len(stock_prices) < 2:
        raise Exception('stock price list must be at least 2 items long')

    highest_profit = None
    for i, stock_price_purchased in enumerate(stock_prices):
        for stock_price_sold in stock_prices[i + 1:]:
            profit = stock_price_sold - stock_price_purchased
            if not highest_profit or profit > highest_profit:
                highest_profit = profit

    return highest_profit


def stock_prices_2_greedy(stock_prices):
    """
    Solution: Iterate through stock prices once, keeping track of the
    highest profit and lowest buy.
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    if len(stock_prices) < 2:
        raise Exception('stock price list must be at least 2 items long')

    lowest_buy = None
    highest_profit = None
    for stock_price in stock_prices:
        # If this is the first stock price, record it as the lowest buy and
        # move on to the next stock price
        if not lowest_buy:
            lowest_buy = stock_price
            continue

        # Record profit if we sell at the current price after buying at the
        # lowest buying price we've seen yet
        profit = stock_price - lowest_buy

        # If this profit is greater than our highest profit thus far, save it
        # as the new highest profit
        if not highest_profit or profit > highest_profit:
            highest_profit = profit

        # If the current price is lower than our lowest buy, then record it
        # as the new lowest buy
        if lowest_buy > stock_price:
            lowest_buy = stock_price
    return highest_profit
