import sys
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)

stdoutHandler = logging.StreamHandler(stream=sys.stdout)
fileHandler = logging.FileHandler("logs.txt")

stdoutFmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"
)

jsonFmt = jsonlogger.JsonFormatter(
    "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
    rename_fields={"levelname": "severity", "asctime": "timestamp"},
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)

stdoutHandler.setFormatter(stdoutFmt)
fileHandler.setFormatter(jsonFmt)

logger.addHandler(stdoutHandler)
logger.addHandler(fileHandler)

logger.setLevel(logging.DEBUG)

logger.debug("A debug message")
logger.error("An error message")
