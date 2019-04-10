#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/10 上午 09:29

import logging

logger = logging.getLogger('root.test')
# logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(message)s')
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.WARNING)
# logger.addHandler(console_handler)



logging.debug('debug')
logging.info('info')
logging.warning('waining')
logging.critical('critical')




# logger.debug('debug')  # 不会记录
# logger.info('info')  # 不会记录
# logger.warning('warning')  # 记录warning
# logger.error('error')  # 记录error
# logger.critical('critical')