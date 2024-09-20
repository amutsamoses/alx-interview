#!/usr/bin/python3
"""
Make change task
"""


def makeChange(coins, total):
    """
    minimum number of coins needed to make change.

    Args:
        coins (list): A list of available coin denominations.
        total (int): The amount of change required.
    Returns:
        int: The minimum number of coins needed to make the total. If it's
        not possible to meet the total with the given coins, returns -1.
    """

    '# If the total is less than or equal to 0, no coins are needed'
    if total <= 0:
        return 0

    '# Sort the coins in descending order'
    coins.sort(reverse=True)
    '# Initialize the counter for the number of coins needed'
    coins_needed = 0
    '# Iterate through each coin denomination'
    for coin in coins:
        '# If the current coin can be used'
        if total / coin > 0:
            '# Add the number of times the current coin'
            coins_needed += total // coin
            '# Update the total to the remaining amount'
            total = total % coin
        '# If the total becomes zero, break out of the loop early'
        if not total:
            break

    '# return -1 (not possible to make change)'
    if total != 0 or coins_needed == 0:
        return -1

    '# Return the total number of coins needed'
    return coins_needed
