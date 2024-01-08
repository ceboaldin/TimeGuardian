import time
import logging
import psutil
from functools import wraps
from .logging_conf import configure_logging

# Global logger instance
logger = logging.getLogger("TimeGuardian")
configure_logging()

class TimeGuardian:
    @staticmethod
    def measure(_func=None, *, name=None, logTimeLimit=None, logMemoryLimit=None):
        """
        A decorator to measure and log the execution time and memory usage of a function. Logs only if execution time or memory usage exceeds the specified limits.

        Parameters:
        _func (callable, optional): The function to be decorated.
        name (str, optional): A custom name to log with the execution time and memory usage.
        logTimeLimit (int, optional): The execution time limit in milliseconds. Logs only if the execution time exceeds this limit.
        logMemoryLimit (int, optional): The memory usage limit in bytes. Logs only if the memory usage exceeds this limit.

        Returns:
        callable: A wrapper function that adds time and memory measurement functionality.

        Usage:
        @TimeGuardian.measure
        def my_function():
            # function implementation

        @TimeGuardian.measure(name="CustomName")
        def another_function():
            # function implementation

        @TimeGuardian.measure(logTimeLimit=200, logMemoryLimit=1024) # logTimeLimit is in milliseconds, logMemoryLimit is in bytes
        def limited_function():
            # function implementation
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                start_memory = psutil.Process().memory_info().rss
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    end_time = time.time()
                    end_memory = psutil.Process().memory_info().rss
                    logger.error(f"Exception in {func.__name__}: {e}")
                    elapsed_time = (end_time - start_time) * 1000
                    memory_usage = end_memory - start_memory
                    if logTimeLimit is None or elapsed_time > logTimeLimit:
                        logger.info(f"Elapsed time until exception: {elapsed_time:.3f}ms")
                    if logMemoryLimit is None or memory_usage > logMemoryLimit:
                        logger.info(f"Memory usage until exception: {memory_usage} bytes")
                    raise
                else:
                    end_time = time.time()
                    end_memory = psutil.Process().memory_info().rss
                    elapsed_time = (end_time - start_time) * 1000
                    memory_usage = end_memory - start_memory
                    if logTimeLimit is None or elapsed_time > logTimeLimit:
                        log_message = f'{name} - ' if name else ''
                        log_message += f'Elapsed time: {elapsed_time:.3f}ms'
                        logger.info(log_message)
                    if logMemoryLimit is None or memory_usage > logMemoryLimit:
                        log_message = f'{name} - ' if name else ''
                        log_message += f'Memory usage: {memory_usage} bytes'
                        logger.info(log_message)

                    return result
            return wrapper

        if _func is None:
            return decorator
        else:
            return decorator(_func)
