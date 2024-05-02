import sys
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)

fmt = jsonlogger.JsonFormatter(
    "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
    rename_fields={"levelname": "severity", "asctime": "timestamp"},
)


stdout.setFormatter(fmt)
logger.addHandler(stdout)

logger.setLevel(logging.INFO)

logger.info("An info")
logger.warning("A warning")
logger.error("An error")
