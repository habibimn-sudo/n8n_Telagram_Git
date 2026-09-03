"""
Utility math functions.

این فایل شامل توابع کمکی ریاضی است. تابع factorial به این فایل اضافه شده است.
"""
from typing import Any

__all__ = ["factorial"]


def factorial(n: int) -> int:
    """
    محاسبه فاکتوریل عدد صحیح غیرمنفی n و بازگشت مقدار آن.

    پارامترها:
        n (int): عدد صحیح غیرمنفی

    بازگشت:
        int: مقدار فاکتوریل n

    خطاها:
        TypeError: اگر n از نوع int نباشد
        ValueError: اگر n منفی باشد

    مثال:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    # نوع ورودی را بررسی می‌کنیم
    if not isinstance(n, int):
        raise TypeError("n باید از نوع int باشد")
    if n < 0:
        raise ValueError("n باید عددی غیرمنفی باشد")

    # محاسبه به صورت تکراری (برای جلوگیری از محدودیت عمق بازگشتی)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
