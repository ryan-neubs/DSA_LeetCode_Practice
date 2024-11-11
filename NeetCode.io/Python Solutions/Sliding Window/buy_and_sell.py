def get_max_profit(prices):
    curr_max = 0
    l = 0
    r = 1
    while r < len(prices):
        curr_max = max(curr_max, prices[r] - prices[l])
        if prices[r] < prices[l]:
            l = r
        r += 1

    return curr_max


print(get_max_profit([5,1,5,6,7,1,10]))