
from  log_base import *
from logging_test2 import *
import traceback
import numpy as np

logging.info('this is a info')


try:
  fun()
except Exception as err:
    print(err)
    print(traceback.format_exc())
    logging.warning('im wrong')
    logging.critical(traceback.format_exc())