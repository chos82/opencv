from ccm import OCVDetector as cvd

import os
import numpy as np
import cv2 as cv

import logging


# create logger with 'spam_application'
logger = logging.getLogger('cam-cap-starter')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('cam-cap-starter.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
        
sep = '--------------------------------------'
logger.info(sep)
logger.info('starting cam capture manipulator')
logger.info(sep)

path = os.path.abspath(cv.__file__)
logger.info('path of OpenCV library:')
logger.info(path)
    
Det = cvd.OCVDetector()
try:
    Det.run()
except:
    exit(-1)
