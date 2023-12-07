#!/usr/bin/python3
""" The functio is winner """


def isWinner(x, nums):
    """ The main function is winner """

    def calculate_primes(n):
        """ Function used to calculate primes """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def is_prime(num):
        """ checking whether the number is prime or not """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_winner(round_nums):
        """ Finding the winner between the two """
        maria_turn = True
        for num in round_nums:
            if is_prime(num):
                if maria_turn:
                    return "Ben"
                maria_turn = not maria_turn
        return "Maria"

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = calculate_primes(n)
        winner = get_winner(primes)
        wins[winner] += 1

    max_wins = max(wins.values())

    if wins["Maria"] == wins["Ben"]:
        return None
    elif wins["Maria"] == max_wins:
        return "Maria"
    else:
        return "Ben"
