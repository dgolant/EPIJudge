from typing import List

from test_framework import generic_test

# [310,315,275,295,260,270,290,230,255,250] -> 30 (290-260)
def buy_and_sell_stock_once(prices: List[float]) -> float:
    # max profit starts at 0
    # lowest cost starts at INF
    # iterate over the values
    # if $PRICE < LC, LC == COST
    # ELSE IF $PRICE > LC, max profit == math.max(max_profit, $PRICE-LC)
    max_profit = 0.0
    lowest_cost = float('inf')

    for i in range(len(prices)):
        price = prices[i]
        if price < lowest_cost:
            lowest_cost = price
        if price > lowest_cost:
            max_profit = max(max_profit, price-lowest_cost)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
