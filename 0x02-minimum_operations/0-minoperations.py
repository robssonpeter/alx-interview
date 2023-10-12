#!/usr/bin/python3
""" The module to find the minimum operations """


def minOperations(n):
    """ If n is less than or equal to 1, it's impossible to achieve,
    so return 0."""
    if n <= 1:
        return 0

    """ Initialize the count of operations to 0. """
    operations = 0
    """ Start with the smallest prime factor, which is 2. """
    divisor = 2

    """ Keep looping until n becomes 1,
    meaning we've achieved the desired number of H characters. """
    while n > 1:
        """ Check if the current divisor is a prime factor of n. """
        while n % divisor == 0:
            """ If it is, divide n by the divisor,
            and add the divisor to the operations count. """
            n //= divisor
            operations += divisor

        """ Move to the next potential
        prime factor (increment divisor). """
        divisor += 1

    """ Return the total number of operations
    needed to achieve n H characters. """
    return operations
