#!/usr/bin/python3
""" The module for python """


def makeChange(coins, total):
    """ The Make change function
    to determine the lowest number of coins
    """
    coins = sorted(coins)
    """ Make the array reversed after sorting it """
    coins.reverse()
    coin_count = 0
    added = 0
    current_index = 0
    while (current_index <= len(coins)):
        if current_index >= len(coins):
            break
        if current_index == len(coins) - 1:
            if total - added < coins[current_index]:
                coin_count = -1
                break
        if total - added > coins[current_index]:
            added = added + coins[current_index]
            coin_count = coin_count + 1
        else:
            current_index = current_index + 1

    return coin_count
