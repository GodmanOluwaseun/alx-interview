#!/usr/bin/python3
"""0-prime_game
Dtermnines winner of game across x rounds, when no prime is left.
"""

def isWinner(x, nums):
    """Determines winner of game

    Args:
        x (int): No of rounds.
        nums (list of int): List of numbers for each round.

    Returns:
        str: Winner of game.
    """

    if not nums or x < 1:
        return None

    maxn = max(nums)

    def prime_filter(maxn):
        """Filters list for primes"""
        prime = [True] * (maxn + 1)
        prime[0] = prime[1] = False
        p = 2
        while p * p <= maxn:
            if prime[p]:
                for i in range(p * p, maxn + 1, p):
                    prime[i] = False
            p += 1
        return [i for i in range(maxn + 1) if prime[i]]

    primes = prime_filter(maxn)

    prime_count = [0] * (maxn + 1)
    for i in range(maxn + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)
    
    maria_win, ben_win = 0, 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_win += 1
        else:
            maria_win += 1

    if maria_win > ben_win:
        return "Maria"
    elif ben_win > maria_win:
        return "Ben"
    else:
        return None