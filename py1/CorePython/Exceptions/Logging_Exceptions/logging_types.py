import logging

logging.basicConfig(filename="mylog1", level=logging.ERROR)

logging.error('There is an error in the program')
logging.critical('There is a problem in the design')
logging.warning('The project is going slow')
logging.info('You are a junior programmer')
logging.debug('Line no. 10 has syntax error')
