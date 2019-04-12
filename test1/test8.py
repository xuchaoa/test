#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/11 下午 08:58

a = {'name':'archerx','sex':'man'}
b = {'xxx':'xxx'}
a.update(b)

print(a)

b.update(b)
print(b)


print(a.items())

b = 'this is the new'