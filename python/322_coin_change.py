# https://leetcode.com/problems/coin-change/submissions/859937984/
# We'll calculate the amount from 1-amount and store that in an array. By default, we'll set all these values to
# one beyond the amount since we want the min number of coins. For every amount, we'll go through each coin and subtract
# the coin value from the amount. If it's greater than 0, we then get the remainder / index in the DP array and add
# one to that value and update. At the end, we return the DP[amount] only if it's less than the default value we
# placed in the array.

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for amt in range(1, amount + 1):
        for coin in coins:
            if amt - coin >= 0:
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)
    return dp[amount] if dp[amount] < amount + 1 else -1


print(coinChange([1, 2, 5], 11))
