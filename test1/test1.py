#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/1/26 下午 03:33
import os
a = 'archerx'

def test():
    print('this is the test.')

class test1(object):
    def __init__(self):
        pass

class test2(test1):
    def __init__(self):
        pass

print(test.__globals__)
print(test.__globals__['__builtins__'].eval("print('yes')"))   #
print(test.__class__)  #返回调用的参数类型   <class 'function'>
print(test1.__bases__)  #返回该类的基类   (<class 'object'>,)
print(test1.__subclasses__())  #返回该类的子类   [<class '__main__.test2'>]
#jinja2获取积累的方法有下面几种（先获取当前类然后向后追溯）：
print(''.__class__.__mro__)  #(<class 'str'>, <class 'object'>)
print(''.__class__.__mro__[1])  #<class 'object'>
#下面这几个用__bases__或者__mro__都能获取基类
print({}.__class__.__bases__[0])    #<class 'object'>
print(().__class__.__bases__[0])   #<class 'object'>
print([].__class__.__bases__[0])    #<class 'object'>