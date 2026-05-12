"""Mathematical utility functions for common calculations."""

import math
from collections.abc import Generator

__all__: list[str] = [
    "is_prime",
    "is_factorial",
    "gcd",
    "lcm",
    "fibonacci",
    "fibonacci_sequence",
    "is_perfect_square",
    "is_even",
    "is_odd",
    "is_power_of_two",
]


def is_prime(n: int) -> bool:
    """Return whether *n* is a prime number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_factorial(n: int) -> tuple[bool, int | None]:
    """Return ``(True, k)`` if *n* equals *k*!, else ``(False, None)``."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return (False, None)
    if n == 1:
        return (True, 0)
    i = 2
    factorial = 1
    while factorial < n:
        factorial *= i
        i += 1
    if factorial == n:
        return (True, i - 1)
    return (False, None)


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of *a* and *b*."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of *a* and *b*."""
    return math.lcm(a, b)


def fibonacci(n: int) -> int:
    """Return the *n*-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(n: int) -> Generator[int, None, None]:
    """Yield the first *n* Fibonacci numbers."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 0:
        return
    a, b = 0, 1
    yield a
    if n == 1:
        return
    yield b
    for _ in range(2, n):
        a, b = b, a + b
        yield b


def is_perfect_square(n: int) -> bool:
    """Return whether *n* is a perfect square."""
    if n < 0:
        raise ValueError("n must be non-negative")
    root = math.isqrt(n)
    return root * root == n


def is_even(n: int) -> bool:
    """Return whether *n* is even."""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Return whether *n* is odd."""
    return n % 2 != 0


def is_power_of_two(n: int) -> bool:
    """Return whether *n* is a positive power of two."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n > 0 and (n & (n - 1)) == 0
