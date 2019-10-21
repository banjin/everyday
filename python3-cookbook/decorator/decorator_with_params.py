"""
带有参数的装饰器
"""

from functools import wraps


def decorator_name(level=1):
    def real_deactor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # do somethings
            func(*args, **kwargs)

            # do other things
        return wrapper
    return real_deactor

