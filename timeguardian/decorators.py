
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
    """
    A utility class for measuring and monitoring the performance of functions.

    Attributes:
        time_unit (str): The unit of time used for measuring elapsed time (default: 'ms').
        memory_unit (str): The unit of memory used for measuring memory usage (default: 'bytes').
    """

    time_unit = 'ms'  # default unit milliseconds
    memory_unit = 'bytes'  # default unit bytes

    @classmethod
    def set_time_unit(cls, unit):
        """
        Set the unit of time used for measuring elapsed time.

        Args:
            unit (str): The unit of time ('ms' for milliseconds, 's' for seconds, etc.).
        """
        cls.time_unit = unit

    @classmethod
    def set_memory_unit(cls, unit):
        """
        Set the unit of memory used for measuring memory usage.

        Args:
            unit (str): The unit of memory ('bytes', 'KB', 'MB', etc.).
        """
        cls.memory_unit = unit

    @staticmethod
    def convert_time(time_in_seconds):
        """
        Convert the given time from seconds to the configured time unit.

        Args:
            time_in_seconds (float): The time in seconds.

        Returns:
            float: The converted time.
        """
        if TimeGuardian.time_unit == 'ms':
            return time_in_seconds * 1000
        elif TimeGuardian.time_unit == 's':
            return time_in_seconds
        # Add more unit conversions here

    @staticmethod
    def convert_memory(memory_in_bytes):
        """
        Convert the given memory from bytes to the configured memory unit.

        Args:
            memory_in_bytes (int): The memory in bytes.

        Returns:
            float: The converted memory.
        """
        if TimeGuardian.memory_unit == 'bytes':
            return memory_in_bytes
        elif TimeGuardian.memory_unit == 'KB':
            return memory_in_bytes / 1024
        elif TimeGuardian.memory_unit == 'MB':
            return memory_in_bytes / (1024 * 1024)
        # Add more unit conversions here

    @staticmethod
    def _measure_performance(start_time, start_memory, elapsed, memory, name):
        """
        Measure and log the performance of a function.

        Args:
            start_time (float): The start time of the function execution.
            start_memory (int): The start memory usage.
            elapsed (bool): Whether to measure and log the elapsed time.
            memory (bool): Whether to measure and log the memory usage.
            name (str): The name of the function (optional).

        Returns:
            None
        """
        log_message = f'{name} - ' if name else ''
        if memory:
            end_memory = psutil.Process().memory_info().rss
            memory_usage = TimeGuardian.convert_memory(end_memory - start_memory)
            log_message += f'Memory usage: {memory_usage} {TimeGuardian.memory_unit}'
        if elapsed:
            end_time = time.time()
            elapsed_time = TimeGuardian.convert_time(end_time - start_time)
            if memory:
                log_message += ', '
            log_message += f'Elapsed time: {elapsed_time} {TimeGuardian.time_unit}'
        logger.info(log_message)

    @staticmethod
    async def _async_wrapper(func, name, elapsed, memory, *args, **kwargs):
        """
        Asynchronous wrapper function for measuring and monitoring a function.

        Args:
            func (callable): The function to be wrapped.
            name (str): The name of the function (optional).
            elapsed (bool): Whether to measure and log the elapsed time.
            memory (bool): Whether to measure and log the memory usage.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The result of the wrapped function.
        """
        start_time = time.time() if elapsed else None
        start_memory = psutil.Process().memory_info().rss if memory else None
        try:
            result = await func(*args, **kwargs)
        finally:
            if elapsed or memory:
                TimeGuardian._measure_performance(start_time, start_memory, elapsed, memory, name)
        return result

    @staticmethod
    def _sync_wrapper(func, name, elapsed, memory, *args, **kwargs):
        """
        Synchronous wrapper function for measuring and monitoring a function.

        Args:
            func (callable): The function to be wrapped.
            name (str): The name of the function (optional).
            elapsed (bool): Whether to measure and log the elapsed time.
            memory (bool): Whether to measure and log the memory usage.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The result of the wrapped function.
        """
        start_time = time.time() if elapsed else None
        start_memory = psutil.Process().memory_info().rss if memory else None
        try:
            result = func(*args, **kwargs)
        finally:
            if elapsed or memory:
                TimeGuardian._measure_performance(start_time, start_memory, elapsed, memory, name)
        return result

    @staticmethod
    def measure(_func=None, *, name: str = None, elapsed: bool = True, memory: bool = False) -> callable:
        """
        Decorator for measuring the performance of a function.

        Args:
            _func (callable): The function to be decorated (optional).
            name (str): The name of the function (optional).
            elapsed (bool): Whether to measure and log the elapsed time.
            memory (bool): Whether to measure and log the memory usage.

        Returns:
            callable: The decorated function.
        """
        def decorator(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                return await TimeGuardian._async_wrapper(func, name, elapsed, memory, *args, **kwargs)

            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                return TimeGuardian._sync_wrapper(func, name, elapsed, memory, *args, **kwargs)

            if asyncio.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper

        if _func is None:
            return decorator
        else:
            return decorator(_func)

    @staticmethod
    def monitor(_func=None, *, name: str = None, elapsed: int = None, memory: int = None) -> callable:
        """
        Decorator for monitoring the performance of a function.

        Args:
            _func (callable): The function to be decorated (optional).
            name (str): The name of the function (optional).
            elapsed (int): The interval in seconds to measure and log the elapsed time (optional).
            memory (int): The interval in seconds to measure and log the memory usage (optional).

        Returns:
            callable: The decorated function.
        """
        def decorator(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                return await TimeGuardian._async_wrapper(func, name, elapsed, memory, *args, **kwargs)

            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                return TimeGuardian._sync_wrapper(func, name, elapsed, memory, *args, **kwargs)

            if asyncio.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper

        if _func is None:
            return decorator
        else:
            return decorator(_func)
    