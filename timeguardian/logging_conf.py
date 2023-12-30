from logging.config import dictConfig


def configure_logging() -> None:
    """
    Configures the logging for the application.
    
    Sets up a logger with a specific format and handler using the 'rich' logging module.
    The logger is configured to display messages with a timestamp.
    """
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(message)s",
                },
            },
            "handlers": {
                "default": {
                    "class": "rich.logging.RichHandler",
                    "level": "DEBUG",
                    "formatter": "console",
                    "show_path": False,
                    "rich_tracebacks": True,
                },
            },
            "loggers": {
                "TimeGuardian": {
                    "handlers": ["default"],
                    "level": "DEBUG",
                    "propagate": False
                }
            }
        }
    )