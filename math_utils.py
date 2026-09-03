"""math_utils.py

Collection of math utility functions.
"""

__all__ = ['factorial']


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n (n!).

    Examples:
        factorial(0) == 1
        factorial(5) == 120

    Raises:
        TypeError: if n is not an int.
        ValueError: if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
