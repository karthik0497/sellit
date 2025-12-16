import logging
import sys
from pathlib import Path

# Setup logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Define Formatter
FORMATTER = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)-10s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def _setup_logger(name: str, log_file: str, level=logging.INFO):
    """Internal helper to set up a logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False # Prevent double logging if attached to root

    # Check if handlers are already added to avoid duplicates
    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(LOG_DIR / log_file)
        file_handler.setFormatter(FORMATTER)
        logger.addHandler(file_handler)

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        logger.addHandler(console_handler)

    return logger

# Create specific loggers
_db_logger = _setup_logger("DB_LOG", "database.log")
_api_logger = _setup_logger("API_LOG", "api.log")
_app_logger = _setup_logger("APP_LOG", "app.log")

def log_db(message: str, level: str = "info"):
    """
    Log database related events.
    Usage: log_db("Connection successful")
    """
    lvl = getattr(logging, level.upper(), logging.INFO)
    _db_logger.log(lvl, message)

def log_api(message: str, level: str = "info"):
    """
    Log API request/response events.
    Usage: log_api("Received GET /users", level="debug")
    """
    lvl = getattr(logging, level.upper(), logging.INFO)
    _api_logger.log(lvl, message)

def log_app(message: str, level: str = "info"):
    """
    General application logs.
    """
    lvl = getattr(logging, level.upper(), logging.INFO)
    _app_logger.log(lvl, message)
