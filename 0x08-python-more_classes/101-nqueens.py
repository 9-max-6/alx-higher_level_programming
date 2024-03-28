#!/usr/bin/python3
import sys

def is_safe(col, queens, diag, anti_diag):
    return col not in queens and diag not in diag and anti_diag not in anti_diag

def recursive_solve(n, row, queens, diag, anti_diag, solutions, current_solution):
    if row == n:
        solutions.append(current_solution[:])
        return

    for col in range(n):
        d = row - col
        a_d = row + col
        if is_safe(col, queens, d, a_d):
            queens.add(col)
            diag.add(d)
            anti_diag.add(a_d)
            current_solution.append([row, col])

            recursive_solve(n, row + 1, queens, diag, anti_diag, solutions, current_solution)

            queens.remove(col)
            diag.remove(d)
            anti_diag.remove(a_d)
            current_solution.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    n = int(sys.argv[1])
    solutions = []
    recursive_solve(n, 0, set(), set(), set(), solutions, [])
    for sol in solutions:
        print(sol)
