import time
import logging
from functools import wraps
from .logging_conf import configure_logging

# Global logger instance
logger = logging.getLogger("TimeGuardian")
configure_logging()

class TimeGuardian:
    @staticmethod
    def measure(_func=None, *, name=None, logTimeLimit=None):
        """
        A decorator to measure and log the execution time of a function. Logs only if execution time exceeds logTimeLimit.

        Parameters:
        _func (callable, optional): The function to be decorated.
        name (str, optional): A custom name to log with the execution time.
        logTimeLimit (int, optional): The execution time limit in milliseconds. Logs only if the execution time exceeds this limit.

        Returns:
        callable: A wrapper function that adds time measurement functionality.

        Usage:
        @TimeGuardian.measure
        def my_function():
            # function implementation

        @TimeGuardian.measure(name="CustomName")
        def another_function():
            # function implementation

        @TimeGuardian.measure(logTimeLimit=200) # logTimeLimit is in milliseconds 
        def limited_function():
            # function implementation
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    end = time.time()
                    logger.error(f"Exception in {func.__name__}: {e}")
                    elapsed_time = (end - start) * 1000
                    if logTimeLimit is None or elapsed_time > logTimeLimit:
                        logger.info(f"Elapsed time until exception: {elapsed_time:.3f}ms")
                    raise
                else:
                    end = time.time()
                    elapsed_time = (end - start) * 1000
                    if logTimeLimit is None or elapsed_time > logTimeLimit:
                        log_message = f'{name} - ' if name else ''
                        log_message += f'Elapsed time: {elapsed_time:.3f}ms'
                        logger.info(log_message)

                    return result
            return wrapper

        if _func is None:
            return decorator
        else:
            return decorator(_func)