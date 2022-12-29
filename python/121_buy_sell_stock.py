# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Use two pointers, one at index 0 (l) and one at index 1 (r). r will always be increased.
# At each iteration, calculate the profit and update the max.
# Check to see if the value at r is less than the value at l. If it is, we move the l pointer up to r.

def maxProfit(prices):
    l = 0
    r = 1
    max_price = 0

    while r < len(prices):
        max_price = max(max_price, prices[r] - prices[l])
        if prices[r] < prices[l]:
            l = r
        r += 1
    return max_price
