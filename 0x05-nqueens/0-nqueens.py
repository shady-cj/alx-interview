#!/usr/bin/python3
import sys
"""
A module that contains a function that performs backtracking
to return the number of valid placing for Non-attacking queens
"""


def nqueens(N, col, not_safe=set([]), main=0):
    """
    The nqueens function performs recursive backtracking to
    print out the various combinations for the a non-attacking
    queens of NxN chessboard
    """
    if col >= N:
        return [[]]

    init = set(not_safe)
    solution = []
    possibilities = []
    for i in range(N):
        if (col, i) not in not_safe:
            solution.append([col, i])
            c = col
            rf = rb = i

            while c < N - 1:
                c += 1
                rf += 1
                not_safe.add((c, i))
                not_safe.add((c, rf))
                if rb >= 1:
                    rb -= 1
                    not_safe.add((c, rb))
            mat = nqueens(N, col + 1, not_safe)
            if mat is not None:
                for possible in mat:
                    possibilities.append(solution + possible)
                solution = []
            else:
                solution.pop()
            not_safe.clear()
            not_safe.update(init)
    if main:
        for p in possibilities:
            print(p)
    if len(possibilities) > 0:
        return possibilities
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except (TypeError, ValueError):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n, 0, main=1)
