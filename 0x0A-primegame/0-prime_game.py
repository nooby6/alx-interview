#!/usr/bin/python3
"""prime game module"""


def generate_primes(n):
    """
    Returns a list of prime numbers up to n (inclusive).
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
    Determines the winner of the prime game.
    
    Parameters:
    x (int): the number of rounds
    nums (list): list of integers representing the upper limit for each round
    
    Returns:
    str: the name of the player with the most wins, or None if it's a tie
    """
    if not nums or x < 1 or len(nums) < x:
        return None
    
    wins = {"ben": 0, "maria": 0}  # Dictionary to keep track of wins for each player
    i = 0

    while i < x:
        primes = generate_primes(nums[i])  # Generate primes up to nums[i]
        if len(primes) % 2 == 0:  # If the number of primes is even, Ben wins the round
            wins["ben"] += 1
        else:  # If the number of primes is odd, Maria wins the round
            wins["maria"] += 1
        i += 1

    if wins["ben"] > wins["maria"]:
        return 'Ben'
    elif wins["maria"] > wins["ben"]:
        return 'Maria'
    else:
        return None
    