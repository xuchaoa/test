#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/10 上午 08:15

class people:
    country = 'china'
    def __init__(self,name):
        self.country = name
    def pp_info(self):
        print('this is the person info')


obj = getattr(people,'countr',False)
print(obj)

# a = getattr(people,'pp_info')
# a()