#!/usr/bin/python3
"""
This module contains the function minOperations
"""

def divideOp(current, clipboard, n,numOp):
    """
    The function implements divide and conquer
    to get the min operation
    """
    if current == n:
        return numOp
    if current > n:
        return 0
    if clipboard == 0:
        ## copy the first H if there isn't value on clipboard
        numOp += 1
        clipboard += 1

    # copy all and paste
    copypaste = divideOp(current + current, current, n, numOp + 2)
    # paste
    paste = divideOp(current + clipboard, clipboard, n, numOp +1)
    if paste == 0:
        return copypaste
    elif copypaste == 0:
        return paste
    return min(copypaste, paste)

def minOperations(n):
    """
    returns the min possible number of operations
    to achieve exactly n H
    Description of task is present in README
    """
    return divideOp(1, 0, n, 0)
