from logging import getLogger
from logging.config import fileConfig

fileConfig('./logging.conf')
logger = getLogger(__name__)

logger.info('Output only to the console.')
logger.error('Will also be sent to email.')
