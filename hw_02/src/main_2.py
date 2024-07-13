def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("...")
    if n < 0:
        raise ValueError("...")

    result = 1

    for i in range(2, n+1, 1):
        result *= i

    return result


def fibonacci(n: int) -> list:
    if not isinstance(n, int):
        raise TypeError("...")
    if n < 0:
        raise ValueError("...")

    if n == 0:
        return [0]

    result = [0, 1, 1]

    while result[-1] + result[-2] < n:
        result.append(result[-1] + result[-2])

    return result


def count_ones(n: int) -> int:
    counter = 0
    num = n

    while num > 0:
        if num & 1 == 1:
            counter += 1

        num >>= 1

    return counter
