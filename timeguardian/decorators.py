# decorators.py
import time
import logging
from .logging_conf import configure_logging
from functools import wraps


# Global logger instance
logger = logging.getLogger("TimeGuardian")
configure_logging()


def time_func(_func=None, *, name=None):
    """
    A decorator to measure and log the execution time of a function.
    
    Parameters:
    _func (callable, optional): The function to be decorated. If not provided, the decorator can be used with arguments.
    name (str, optional): A custom name to log with the execution time. If not provided, only the time is logged.
    
    Returns:
    callable: A wrapper function that adds time measurement functionality to the decorated function.
    
    Usage:
    @time_func
    def my_function():
        # function implementation
        
    @time_func(name="CustomName")
    def another_function():
        # function implementation
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed_time = (end - start) * 1000

            if name:
                logger.info(f'{name} - Elapsed time: {elapsed_time:.3f}ms')
            else:
                logger.info(f'Elapsed time: {elapsed_time:.3f}ms')

            return result
        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)