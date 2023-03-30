#!/usr/bin/python3
"""
A module that implements lockboxes
"""


def canUnlockAll(boxes):
    """
    Using stacks to implement the lockboxes
    """
    if len(boxes) == 0:
        return True
    stack = [0]
    visited = set([])

    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            stack.extend(boxes[current])
            visited.add(current)
    n = len(boxes)
    for i in range(n):
        if i not in visited:
            return False
    return True
