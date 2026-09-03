def factorial(n):
    """Return the factorial of a non-negative integer n.

    Args:
        n (int): non-negative integer whose factorial is to be computed.

    Returns:
        int: n! (1 for n == 0).

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
