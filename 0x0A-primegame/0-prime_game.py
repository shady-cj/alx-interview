#!/usr/bin/python3
"""
Contains a function isWinner() that
implements the prime game
"""


def findPrime(nums):
    """
    Find and return the first prime number
    from nums
    """
    for num in nums:
        if num == 1:
            continue
        j = num - 1 if num < 10 else 10
        prime = True
        while j > 1:
            if num % j == 0:
                prime = False
                break
            j -= 1
        if prime:
            return num
    return -1


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    ben = 0
    maria = 0
    if x != len(nums):
        return None
    for num in nums:
        if num == 0:
            continue
        arr = []
        for i in range(num):
            arr.append(i + 1)
        turn = 'Maria'
        while len(arr) > 0:
            currentPrime = findPrime(arr)
            if currentPrime == -1:
                if turn == 'Maria':
                    ben += 1
                else:
                    maria += 1
                break
            numMultiple = currentPrime
            while True:
                try:
                    arr.remove(numMultiple)
                    numMultiple += currentPrime
                except ValueError:
                    break
            if turn == 'Maria':
                turn = 'Ben'
            else:
                turn = 'Maria'
    if ben == maria:
        return None
    elif ben > maria:
        return 'Ben'
    else:
        return 'Maria'
