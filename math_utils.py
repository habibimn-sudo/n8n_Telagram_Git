"""
math_utils.py

Utility math functions.
"""

from typing import Any


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n.

    Parameters
    ----------
    n : int
        Non-negative integer whose factorial to compute.

    Returns
    -------
    int
        n! (n factorial)

    Raises
    ------
    TypeError
        If n is not an integer.
    ValueError
        If n is negative.

    Examples
    --------
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    if not isinstance(n, int):
        raise TypeError("factorial() argument must be an integer")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# alias
fact = factorial

__all__ = ["factorial", "fact"]
