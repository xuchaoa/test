#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/11 上午 08:49
import subprocess

def std_decode(data):
    pass


process = subprocess.Popen("git rev-parse --verify HEAD",
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
stdout, _ = process.communicate()

print(stdout)
print(std_decode(stdout))
print(_)