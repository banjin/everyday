
"""基础的装饰器
不带有参数
"""

from functools import wraps


## 类形式的装饰器
class Deactor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # do something
        self.func(*args, **kwargs)
        # do some other things

## 函数形式装饰器
def dea(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do  something
        func(*args, **kwargs)
        # do other things
    return wrapper