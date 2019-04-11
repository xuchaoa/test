#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/10 下午 03:37

import logging

logger = logging.getLogger('log')
logger.setLevel(level=logging.DEBUG)

handler = logging.FileHandler("log.txt")
handler.setLevel(logging.DEBUG)

console = logging.StreamHandler()  #创建一个handler用于输出控制台
console.setLevel(level=logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)


logger.debug("Do something")
logger.info("Start print log")
logger.warning("Something maybe fail.")
logger.info("Finish")

'''
日志记录大体步骤如下：
创建logger
创建handler
定义formatter
给handler添加formatter
给logger添加handler
'''


#创建一个log儿子
loggerchild = logging.getLogger('log.ch')
loggerchild.warning('child msg') #父类的handler进行输出