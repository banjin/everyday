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


# 装饰器类
def time_this(original_function):  
    print("decorating")  
    def new_function(*args,**kwargs): 
        print("starting timer")  
        import datetime  
        before = datetime.datetime.now()  
        x = original_function(*args,**kwargs)  
        after = datetime.datetime.now()  
        print("Elapsed Time = {0}".format(after-before))  
        return x  
    return new_function

def time_all_class_methods(Cls): 
    class NewCls: 
        def __init__(self,*args,**kwargs): 
            self.oInstance = Cls(*args,**kwargs) 
        def __getattribute__(self,s): 
            try:  
                x = super(NewCls,self).__getattribute__(s) 
            except AttributeError:  
                pass 
            else: 
                return x 
            x = self.oInstance.__getattribute__(s) 
            if type(x) == type(self.__init__): 
                return time_this(x) 
            else: 
                return x 
        return NewCls
@time_all_class_methods
class Foo: 
    def a(self): 
        print("entering a") 
        import time 
        time.sleep(3) 
        print("exiting
         a")
oF = Foo()
oF.a()
# out：

if __name__ == "__main__":
    sum_of_random_nums(100)
