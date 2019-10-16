#!/usr/bin/env python3.7

""""
类装饰器
记录函数运行时间
""""

import time


class time_decorator:
    def __init__(self, f):
        self.f = f
        print(f'Time decorator for {self.f.__name__} created')
    
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.f(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f'Duration of {self.f.__name__} function cail was {duration}')
        return result


@time_decorator
def sum_of_random_nums(n):
    random_nums = list(range(n))
    return sum(random_nums)


if __name__ == "__main__":
    sum_of_random_nums(100)
