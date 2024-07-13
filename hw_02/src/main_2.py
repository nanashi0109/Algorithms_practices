def factorial(n) -> int:
    assert isinstance(n, int), TypeError("...")

    result = 1

    for i in range(2, n+1, 1):
        result *= i

    return result


