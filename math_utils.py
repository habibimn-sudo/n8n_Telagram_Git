"""
math_utils.py

توابع کمکی ریاضی.
"""


def factorial(n: int) -> int:
    """
    محاسبه فاکتوریل عدد صحیح n به صورت تکراری.

    پارامترها:
        n (int): عددی غیرمنفی که فاکتوریل آن محاسبه می‌شود.

    بازگشتی:
        int: مقدار فاکتوریل n (n!).

    استثناها:
        TypeError: اگر n از نوع int نباشد.
        ValueError: اگر n منفی باشد.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
