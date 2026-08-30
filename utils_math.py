"""utils_math.py

توابع کمکی ریاضی.

این ماژول تابع factorial را فراهم می‌کند که فاکتوریل یک عدد صحیح
نامنفی را محاسبه می‌کند.
"""

__all__ = ["factorial"]


def factorial(n: int) -> int:
    """محاسبه فاکتوریل n.

    پارامترها:
    n: عدد صحیح نامنفی.

    بازگشتی:
    حاصل ضرب اعداد صحیح از 1 تا n (n!). برای n=0 مقدار 1 بازمی‌گردد.

    استثناها:
    TypeError: اگر n از نوع int نباشد.
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
