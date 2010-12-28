#!/bin/env python

import sys
import logging
import logging.handlers

LOG_FILENAME = 'example.log'

formatter = logging.Formatter("%(asctime)s %(name)s: [ID %(process)d/%(thread)d] %(levelname)s: %(message)s")

ch = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, 'M', 1)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

logger = logging.getLogger('MyLogger')
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

logger.info('this is a test message')

sys.exit(0)
