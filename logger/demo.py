"""
This demo shows the logging message displayed in console is coloured for different level messages.
Moreover, we also demonstrate the logging timestamp is displayed in ISO8601 format
"""
from timestamp_formatter import get_logger

my_logger = get_logger(__name__)


if __name__ == "__main__":
    my_logger.debug("Testing")
    my_logger.info("Hello World")
    my_logger.warning("Be careful")
    my_logger.error("Something Wrong")
