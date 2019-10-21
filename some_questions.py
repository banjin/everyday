#!/usr/bin/env python
# coding:utf-8

"""
一些比较诡异的问题

#######
>>> x, y = ??
>>> x + y == y + x
False

######
>>> x = ?
>>> x < x
True

######
>>> x, y = ??
>>> min(x, y) == min(y, x)
False


######
>>>  x = ?
>>>len(set(list(x))) == len(list(set(x)))
False


#####
>>> x, s = ??
>>> s.add(x)
>>> type(x) in map(type, s)
False

#####
>>> x, y = ???
>>> x < y and all(a>=b for a, b in zip(x,y))
True

#####
>>> x, y = ??
>>> sum(0 * x, y) == y
False

#####
>>> x = ?
>>> min(x) == min(*x)
False

#####
>>>x, y, z = ???
>>> x *(y * z) == (x*y)*z
False

#####
>>>x, y = ??
>>>y > max(x) and y in x
True

#####
>>>x, y = ??
>>> any(x) and not any(x + y)
True

#####
>>>x, y = ??
>>>x.count(y) <= len(x)
False

#####
>>> x = ?
>>>all(filter(None, x))
False


############### 疑惑的问题 ###############
>>>  1 < 2 == 2
True

#########  
"""
