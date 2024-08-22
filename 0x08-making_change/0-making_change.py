#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of integers of the coins available
        total (int): total number to be met

    Returns:
        int: fewest number of coins needed to meet the total.
        0: if the total is 0 or less.
        -1: if the total cannot be met with the available coins.

    """

    '#0 or less, no coins needed'
    if total <= 0:
        return 0

    '#initialize current sum(check) and coin count(temp)'
    check = 0
    temp = 0

    '#sort the in desc'
    coins.sort(reverse=True)

    '#iterate through each sorted coins'
    for i in coins:

        while check < total:

            check += i

            temp += 1

    '#return coount of coins used if equal'
    if check == total:
        return temp

        '#if check exceed the total, subtract and decrease coin'
        check -= i
        temp -= 1

    '#if no exact coin combination is meet'
    return -1
