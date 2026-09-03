def factorial(n):
    """Return n! (factorial of n) for non-negative integer n. For n == 0 returns 1."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

