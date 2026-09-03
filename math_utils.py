"""ماژول ابزارهای ریاضی ساده.

این ماژول توابع کمکی ریاضی را ارائه می‌دهد. در حال حاضر شامل تابع
factorial برای محاسبه فاکتوریل اعداد صحیح غیرمنفی است.
"""

__all__ = ["factorial"]


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n using an iterative loop.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial n! as an int.

    Raises:
        TypeError: If n is not an int.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
