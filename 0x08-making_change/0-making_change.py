#!/usr/bin/python3
"""
0-making_change.py
"""

def makeChange(coins, total):
    # If the total is negative, return -1 as it's not possible to make change
    if total < 0:
        return -1

    # Initialize a list with total+1 elements, all set to float('inf')
    # This list will store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    dp[0] = 0

    # Iterate over each coin in the list of coins
    for coin in coins:
        # For each coin, update the dp list for all amounts from coin to total
        for amount in range(coin, total + 1):
            # Update the dp value for the current amount
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    # If dp[total] is still float('inf'), it means it's not possible to make change for the total
    # Otherwise, return the minimum number of coins needed for the total
    return dp[total] if dp[total] != float('inf') else -1