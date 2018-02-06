from ic_1_stock_prices import stock_prices_1_brute_force, stock_prices_2_greedy


def test_stock_price_algorithms_lose():
    stock_prices = [10, 9, 7]
    assert stock_prices_1_brute_force(stock_prices) == -1
    assert stock_prices_2_greedy(stock_prices) == -1


def test_stock_price_algorithms_no_gain():
    stock_prices = [2, 2, 1, 1]
    assert stock_prices_1_brute_force(stock_prices) == 0
    assert stock_prices_2_greedy(stock_prices) == 0


def test_stock_price_algorithms_gain_1():
    stock_prices = [1, 2, 3, 4, 5]
    assert stock_prices_1_brute_force(stock_prices) == 4
    assert stock_prices_2_greedy(stock_prices) == 4


def test_stock_price_algorithms_gain_2():
    stock_prices = [10, 7, 5, 8, 11, 9]
    assert stock_prices_1_brute_force(stock_prices) == 6
    assert stock_prices_2_greedy(stock_prices) == 6


def test_stock_price_algorithms_gain_3():
    stock_prices = [9, 8, 10, 7, 11, 6, 12]
    assert stock_prices_1_brute_force(stock_prices) == 6
    assert stock_prices_2_greedy(stock_prices) == 6
