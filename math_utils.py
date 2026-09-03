"""
math_utils - simple mathematical utilities.

This module provides basic math helper functions.
"""

__all__ = ["factorial"]


def factorial(n: int) -> int:
    """Return the factorial of n using an iterative loop.

    Args:
        n (int): Non-negative integer whose factorial to compute.

    Returns:
        int: The factorial of n.

    Raises:
        TypeError: If n is not an int.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
