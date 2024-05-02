import sys
import logging


logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)

fmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s%(lineno)s | %(process)d | %(user)s | %(session_id)s >>> %(message)s"
)

stdout.setFormatter(fmt)
logger.addHandler(stdout)

logger.setLevel(logging.INFO)

logger.info("Info message", extra={"user": "johndoe", "session_id": "abc123"})
logger.warning("Warning message", extra={"user": "joegage", "session_id": "3fe-uz"})
logger.error("Error message", extra={"user": "domingrange", "session_id": "2fe-a1"})
