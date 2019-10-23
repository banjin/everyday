def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    import os
    
    for child in os.listdir(sPath):
        sChildPath = os.path.join(sPath, child)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

"""
阅读下面的代码，写出A0，A1至An的最终值。
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

A0 = {'a':1, 'b':2, 'c':3,'d':4,'e':5}
A1 = [0,1,2,3,4,5,6,7,8,9] # python2
A1 是一个迭代器  # python3
A2 = []
A3 = [1,2,3,4,5]
A4 = [1,2,3,4,5]
A5 = {0:0, 1:1,2:4,3:9:4:16,5:25,6:36,7:49,8:64,9:81}
A6 = [[0,0],[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81]]



def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print l 

>>> f(3)
[0, 1, 4]
>>> f(5,[6,7])  # 传入新的列表，创建的是一个新的列表
[6, 7, 0, 1, 4, 9, 16]
>>> f(2)  # 没有传入列表参数，默认使用的与第一次调用时候同一个的列表对象
[0, 1, 4, 0, 1]



>>> class A(object):
        def go(self):
            print("go A go!")
        def stop(self):
            print("stop A stop!")
        def pause(self):
            raise Exception("Not Implemented")
...
>>> class B(A):
        def go(self):
            super(B, self).go()
            print("go B go!")
...
>>> class C(A):
        def go(self):
            super(C, self).go()
            print("go C go!")
        def stop(self):
            super(C, self).stop()
            print("stop C stop!")
...
>>> class D(B,C):
        def go(self):
            super(D, self).go()
            print("go D go!")
        def stop(self):
            super(D, self).stop()
            print("stop D stop!")
        def pause(self):
            print()"wait D wait!")
...
>>> class E(B,C): pass
...
>>> a = A()
>>> b = B()
>>> c = C()
>>> d = D()
>>> e = E()
>>> a.go()
go A go!
>>> b.go()
go A go!
go B go!
>>> c.go()
go A go!
go C go!
>>> d.go()
go A go!
go C go!
go B go!
go D go!
>>> e.go()
go A go!
go C go!
go B go!
>>> a.stop()
stop A stop!
>>> b.stop()
stop A stop!
>>> c.stop()
stop A stop!
stop C stop!
>>> d.stop()
stop A stop!
stop C stop!
stop D stop!
>>> e.stop()
stop A stop!
stop C stop!
>>> a.pause()
b.pause()
c.pause()
d.pause()
e.pause()Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in pause
Exception: Not Implemented
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in pause
Exception: Not Implemented
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in pause
Exception: Not Implemented
>>> wait D wait!


In [23]: class A():
    ...:     def __init__(self):
    ...:         print('enter A')
    ...:         print('leave A')
    ...:

In [24]: class B(A):
    ...:     def __init__(self):
    ...:         print('enter B')
    ...:         super().__init__()
    ...:         print('leave B')
    ...:

In [25]: class C(A):
    ...:     def __init__(self):
    ...:         print('enter C')
    ...:         super().__init__()
    ...:         print('leave C')
    ...:

In [26]: class D(B, C):
    ...:     def __init__(self):
    ...:         print('enter D')
    ...:         super().__init__()
    ...:         print('leave D')
    ...:

In [27]: d = D()
enter D
enter B
enter C
enter A
leave A
leave C
leave B
leave D

"""


    
