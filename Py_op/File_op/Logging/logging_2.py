import logging
import time
"""
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s')
logger = logging.getLogger(__name__)
#logging.basicConfig(filename='logging_test.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')
logging.debug('End of program')

logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
"""
logger = logging.getLogger(__name__)
logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.critical('Finish updating records')


"""

"""
