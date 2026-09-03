"""Utility math functions."""


def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer n (n!).

    - If n is not an int, raise TypeError.
    - If n is negative, raise ValueError.
    - Use an iterative algorithm (no recursion) to compute the factorial and return an int.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
