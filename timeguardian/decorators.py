# decorators.py
import asyncio
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
    def measure(_func=None, *, name=None, elapsed=True, memory=False):
        """
        A decorator to measure and log the execution time of a function.

        Parameters:
        _func (callable, optional): The function to be decorated.
        name (str, optional): A custom name to log with the execution time.
        elapsed (bool, optional): Flag to enable/disable measuring the elapsed time. Default is True.
        memory (bool, optional): Flag to enable/disable measuring the memory usage. Default is False.

        Returns:
        callable: A wrapper function that adds time measurement functionality.

        Usage:
        @TimeGuardian.measure
        def my_function():
            # function implementation

        @TimeGuardian.measure(name="CustomName")
        def another_function():
            # function implementation
        """
        def decorator(func):
            if asyncio.iscoroutinefunction(func):
                @wraps(func)
                async def wrapper(*args, **kwargs):
                    if elapsed:
                        start_time = time.time()
                    if memory:
                        start_memory = psutil.Process().memory_info().rss
                    try:
                        result = await func(*args, **kwargs)
                    finally:
                        if memory:
                            end_memory = psutil.Process().memory_info().rss
                            memory_usage = end_memory - start_memory
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Memory usage: {memory_usage} bytes'
                            logger.info(log_message)
                        if elapsed:
                            end_time = time.time()
                            elapsed_time = (end_time - start_time) * 1000
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Elapsed time: {elapsed_time:.3f}ms'
                            logger.info(log_message)
                    return result
            else:
                @wraps(func)
                def wrapper(*args, **kwargs):
                    if elapsed:
                        start_time = time.time()
                    if memory:
                        start_memory = psutil.Process().memory_info().rss
                    try:
                        result = func(*args, **kwargs)
                    finally:
                        if memory:
                            end_memory = psutil.Process().memory_info().rss
                            memory_usage = end_memory - start_memory
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Memory usage: {memory_usage} bytes'
                            logger.info(log_message)
                        if elapsed:
                            end_time = time.time()
                            elapsed_time = (end_time - start_time) * 1000
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Elapsed time: {elapsed_time:.3f}ms'
                            logger.info(log_message)
                    return result
            return wrapper

        if _func is None:
            return decorator
        else:
            return decorator(_func)

    @staticmethod
    def monitor(_func=None, *, name=None, elapsed=None, memory=None):
        """
        A decorator to monitor and log the execution time and memory usage of a function. Logs only if execution time or memory usage exceeds the specified limits.

        Parameters:
        _func (callable, optional): The function to be decorated.
        name (str, optional): A custom name to log with the execution time and memory usage.
        elapsed (int, optional): The execution time limit in milliseconds. Logs only if the execution time exceeds this limit.
        memory (int, optional): The memory usage limit in bytes. Logs only if the memory usage exceeds this limit.

        Returns:
        callable: A wrapper function that adds time and memory monitoring functionality.

        Usage:
        @TimeGuardian.monitor(elapsed=200, memory=1024) # elapsed is in milliseconds, memory is in bytes
        def monitored_function():
            # function implementation
        """
        def decorator(func):
            if asyncio.iscoroutinefunction(func):
                @wraps(func)
                async def wrapper(*args, **kwargs):
                    start_time = time.time()
                    start_memory = psutil.Process().memory_info().rss
                    try:
                        result = await func(*args, **kwargs)
                    finally:
                        end_time = time.time()
                        end_memory = psutil.Process().memory_info().rss
                        elapsed_time = (end_time - start_time) * 1000
                        memory_usage = end_memory - start_memory
                        if elapsed is not None and elapsed_time > elapsed:
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Elapsed time: {elapsed_time:.3f}ms'
                            logger.info(log_message)
                        if memory is not None and memory_usage > memory:
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Memory usage: {memory_usage} bytes'
                            logger.info(log_message)
                    return result
            else:
                @wraps(func)
                def wrapper(*args, **kwargs):
                    start_time = time.time()
                    start_memory = psutil.Process().memory_info().rss
                    try:
                        result = func(*args, **kwargs)
                    finally:
                        end_time = time.time()
                        end_memory = psutil.Process().memory_info().rss
                        elapsed_time = (end_time - start_time) * 1000
                        memory_usage = end_memory - start_memory
                        if elapsed is not None and elapsed_time > elapsed:
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Elapsed time: {elapsed_time:.3f}ms'
                            logger.info(log_message)
                        if memory is not None and memory_usage > memory:
                            log_message = f'{name} - ' if name else ''
                            log_message += f'Memory usage: {memory_usage} bytes'
                            logger.info(log_message)

                    return result
            return wrapper

        if _func is None:
            return decorator
        else:
            return decorator(_func)
