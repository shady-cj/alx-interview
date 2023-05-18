#!/usr/bin/python3
"""
a module that contains the makeChange
function
"""


def makeChange(coins, total):
    """
    a function that determines the fewest numbers
    of coins to meet a given amount
    """
    if total <= 0:
        return 0
    n_coins = list(sorted(coins))
    rem = total
    den = n_coins.pop()
    total_coins = 0
    while rem > 0:
        quot = rem // den
        if quot == 0:
            if len(n_coins) == 0:
                return -1
            den = n_coins.pop()
            continue
        total_coins += quot
        rem = rem % den
    return total_coins
