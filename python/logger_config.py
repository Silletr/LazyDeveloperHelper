from loguru import logger

logger.remove()
logger.add(sys.stdout, level="DEBUG")
logger.add(
    "logs/site_log.log",
    rotation="5 MB",
    retention="7 days",
    compression="zip",
    format="{time: DD-MM-YYYY at HH:mm} | {level} | {message}",
    level="DEBUG",
)
