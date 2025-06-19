import logging
from utils.config import LOG_FILE_PATH, LOG_LEVEL

def setup_logging(log_file=LOG_FILE_PATH, log_level=LOG_LEVEL):
    """Sets up logging for the project."""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    logging.basicConfig(
        filename=log_file,
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()

#Example usage:
#logger = setup_logging()
#logger.info("This is an information message")