import logging

logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s', 
    datefmt='%Y-%m-%d %I:%M:%S %p'
)

logger = logging.getLogger(__name__)


print(f'Logger name: {logger.name}')
logger.info('Info')
logger.warning('Warning')


# $ python logger.py
# 07/20/2022 06:48:56 PM Hello warning
# 07/20/2022 06:48:56 PM Goodbye info