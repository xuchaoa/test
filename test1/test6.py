#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/11 上午 11:08


import sys,os

print(sys.platform)
print(os.name)

a = True if (sys.platform in ['win32',] or os.name == 'nt') else False

print(a)

sys.stdout.write('archerx')
sys.stdout.write('archerx')
sys.stdout.flush()

sys.stdout.write('archerx')

print(sys.stdout.encoding)

data = 'xuchao'
b = data.encode(sys.stdout.encoding,'replace')
print(b)

print(data.encode('utf-8'))
import time
print(time.strftime("%X"))

print(sys.argv)
a = sys.argv
print(a)
print(os.path.basename(a[0]))