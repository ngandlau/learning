import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

logger = logging.getLogger(__name__)

logger.warning('Hello warning')
logger.info('Goodbye info')


# $ python logger.py
# 07/20/2022 06:48:56 PM Hello warning
# 07/20/2022 06:48:56 PM Goodbye info