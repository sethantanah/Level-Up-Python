import logging


class CustomLogger:
    def __init__(self):
        pass

    @staticmethod
    def add_logging_level(level_name, level_num, method_name=None):
        if not method_name:
            method_name = level_name.lower()

        if hasattr(logging, level_name) or \
           hasattr(logging, method_name) or \
           hasattr(logging.getLoggerClass(), method_name):
            raise AttributeError(
                "{} already defined in logging module".format(
                    level_name if not hasattr(logging, level_name)
                    else method_name
                )
            )

        def log_for_level(self, message, *args, **kwargs):
            if self.isEnabledFor(level_num):
                self._log(level_num, message, args, **kwargs)

        def log_to_root(message, *args, **kwargs):
            logging.log(level_num, message, *args, **kwargs)

        logging.addLevelName(level_num, level_name)
        setattr(logging, level_name, level_num)
        setattr(logging.getLoggerClass(), method_name, log_for_level)
        setattr(logging, method_name, log_to_root)


# Create an instance of CustomLogger
custom_logger = CustomLogger()

# Create the TRACE level
custom_logger.add_logging_level("TRACE", logging.DEBUG - 5)

# Configure logging
logging.basicConfig(level=logging.TRACE)

# Use the TRACE level
logging.trace("A trace message")
logging.debug("A debug message")
logging.info("An info message")
logging.warning("A warning message")
logging.error("An error message")
logging.critical("A critical message")
