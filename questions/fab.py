#!/usr/bin/env python
# coding:utf-8

"""斐波那契数列
"""


def fabltion(n):
    if n < 2:
        return 1
    return fabltion(n-2) + fabltion(n-1)


def fabltion2(n):
    a, b = 0, 1
    while n:
        yield b
        a, b = b, a + b
        n -= 1


def fabltion3(n):
    """斐波契纳数列1,2,3,5,8,13,21............根据这样的规律
    编程求出400万以内最大的斐波契纳数,并求出它是第几个斐波契纳数。
    n = fabltion3(4000000)
    for i in n:
        print(i)

    """
    a, b = 0, 1
    count = 0
    while b < n:
        yield b
        a, b = b, a + b
        count += 1
    print(count, b)


def add_dict(dict1, dict2):
    """
    实现两个字典的相加，不同的key对应的值保留，相同的key对应的值相加后保留,如果是字符串就拼接
    intput:
        dicta = {"a":1,”b”:2,”c”:3,”d”:4,”f”:”hello” }
        dictb = {“b”:3,”d”:5,”e”:7,”m”:9,”k”:”world”}
    output:
        dictc = {“a”:1,”b”:5,”c”:3,”d”:9,”e”:7,”m”:9,”f”:”hello”,”k”:”world”}

    """
    result = {}
    key1 = set(dict1.keys())
    key2 = set(dict2.keys())
    in_dict1 = list(key1 - key2)
    in_dict2 = list(key2 - key1)
    all_in = key1 & key2
    for i in in_dict1:
        result.update({i: dict1[i]})
    for f in in_dict2:
        result.update({f: dict2[f]})
    for a in all_in:
        t1 = dict1.get(a)
        t2 = dict2.get(a)
        if (isinstance(t1, int) and isinstance(t2, int)) or (isinstance(t1, str) and isinstance(t2, str)): 
            result.update({a: t1+t2})
        elif isinstance(t1, int) and isinstance(t2, str):
            result.update({a: str(t1)+t2})
        elif isinstance(t1, str) and isinstance(t2, int):
            result.update({a: str(t2)+t1})
        else:
            pass
    return result


def taozi():
    """
    海滩上有一堆桃子，五只猴子来分，第一只猴子把这堆桃子平均分成五份，
    多了一个，这只猴子把多的一个扔到了海里，拿走了一份，
    第二只猴子把剩下的把四堆桃子合在一起，
    又平均分成五份，又多了一个，
    它同样把多的一个扔到了海里，
    拿走了一份，第三只，第四只，第五只都是这样做的，
    问海滩上原来最少有多少桃子
    """
    i = 0
    j = 1
    x = 0
    while (i < 5):
        x = 4 * j
        for i in range(0, 5):
            if(x % 4 != 0):
                break
            else:
                i += 1
            x = (x/4) * 5 + 1
        j += 1
    print(x)

    
def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

            

if __name__ == "__main__":
    taozi()
