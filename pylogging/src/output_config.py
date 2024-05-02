import logging

# logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s")
# logging.warning("Something bad is going to happen")

# logging.basicConfig(
#     format="%(levelname)s | %(asctime)s | %(message)s",
#     datefmt="%Y-%m-%dT%H:%M:%SZ",
# )
# logging.warning("Something bad is going to happen")


logging.basicConfig(
    format="%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)

logging.warning("system disk is 85% full")
logging.error("unexpected error")