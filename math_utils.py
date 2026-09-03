def factorial(n):
    """Return the factorial of a non-negative integer n.

    Raises:
        TypeError: if n is not an int.
        ValueError: if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError('n must be an int')
    if n < 0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
