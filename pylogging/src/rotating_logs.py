# Max size Rotation
from logging.handlers import RotatingFileHandler

fileHandler = RotatingFileHandler("logs.txt", backupCount=5, maxBytes=5000000)


# Timed Rotation

from logging.handlers import TimedRotatingFileHandler

fileHandler = TimedRotatingFileHandler(
    "logs.txt", backupCount=5, when="midnight"
)
