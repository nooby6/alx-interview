#!/usr/bin/python3
"""prime game module"""


def generate_primes(n):
    """
    returns a list of primes
    """
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Returns the winner
    """
    if not nums or x < 1 or len(nums) < x:
        return None
    wins = {"ben": 0, "maria": 0}
    i = 0

    while i < x:
        primes = generate_primes(nums[i])
        if len(primes) % 2 == 0:
            wins["ben"] += 1
        else:
            wins["maria"] += 1
        i += 1

    if wins["ben"] > wins["maria"]:
        return 'Ben'
    elif wins["maria"] > wins["ben"]:
        return 'Maria'
    else:
        return None
    