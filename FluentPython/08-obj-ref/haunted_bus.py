
"""不用使用可变类型作为形参的默认值
此方法在传参数时候可以正常运行，但是不传参数，使用默认值时候就会出现问题。
不传参数时候，self.passengers变成了参数默认值的别名。
这是因为默认值是在定义函数时候计算(通常在加载模块时候)，因此默认值变成了函数对象的属性，
因此，如果默认值是可变对象，而且修改了他的值，则后续的函数调用都会受到影响。

>>> bus1 = Bus([1,2,3])
>>> bus1.pick(4)
>>> bus1.drop(1)
>>> bus1.passengers
[2, 3, 4]
>>> bus2 = Bus()
>>> bus2.pick(1)
>>> bus3 = Bus()
>>> bus.passengers
>>> bus3.passengers
"""


class Bus:
    def __init__(self, passengers=[]):
        self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)