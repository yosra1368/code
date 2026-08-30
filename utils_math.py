"""utils_math.py

توابع کمکی ریاضی ساده.
"""

__all__ = ["factorial"]


def factorial(n: int) -> int:
    """محاسبهٔ فاکتوریل یک عدد صحیح نامنفی.

    پارامترها:
        n: عدد صحیح نامنفی که فاکتوریل آن محاسبه می‌شود.

    بازمی‌گرداند:
        فاکتوریل n (عدد صحیح).

    خطاها:
        TypeError: اگر n عدد صحیح نباشد.
        ValueError: اگر n منفی باشد.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
