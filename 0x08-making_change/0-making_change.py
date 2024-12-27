#!/usr/bin/python3
"""
0-making_change:
    Greedy algorithm for solving nnukber of coin problem.
args:
    coins [list]: List of coins available
    total [int]: Total number needed
"""


def makeChange(coins, total):
    """Check no of coins required to make total"""
    if total <= 0:
        return 0

    temp = 0
    check = 0
    coins.sort(reverse=True)

    for coin in coins:
        while check < total:
            check += coin
            temp += 1
        if check == total:
            return temp
        check -= coin
        temp -= 1
    return -1
