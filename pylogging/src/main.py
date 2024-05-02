import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.debug("A debug message")
    logging.info("An info message")
    logging.warning("A warning message")
    logging.error("An error message")
    logging.critical("A critical message")
