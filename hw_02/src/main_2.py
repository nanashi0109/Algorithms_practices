def factorial(n) -> int:
    if not isinstance(n, int):
        raise TypeError("...")
    if n < 0:
        raise ValueError("...")

    result = 1

    for i in range(2, n+1, 1):
        result *= i

    return result


