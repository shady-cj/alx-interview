#!/usr/bin/python3
"""
A module that implements lockboxes
"""


def canUnlockAll(boxes):
    """
    Using stacks to implement the lockboxes
    """
    stack = [0]
    visited = set([])

    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            try:
                stack.extend(boxes[current])
                visited.add(current)
            except:
                continue
    n = len(boxes)
    for i in range(n):
        if i not in visited:
            return False
    return True
