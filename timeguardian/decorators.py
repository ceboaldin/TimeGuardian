
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
    time_unit = 'ms'  # default unit milliseconds
    memory_unit = 'bytes'  # default unit bytes

    @classmethod
    def set_time_unit(cls, unit):
        cls.time_unit = unit

    @classmethod
    def set_memory_unit(cls, unit):
        cls.memory_unit = unit

    @staticmethod
    def convert_time(time_in_seconds):
        if TimeGuardian.time_unit == 'ms':
            return time_in_seconds * 1000
        elif TimeGuardian.time_unit == 's':
            return time_in_seconds
        # Add more unit conversions here

    @staticmethod
    def convert_memory(memory_in_bytes):
        if TimeGuardian.memory_unit == 'bytes':
            return memory_in_bytes
        elif TimeGuardian.memory_unit == 'KB':
            return memory_in_bytes / 1024
        elif TimeGuardian.memory_unit == 'MB':
            return memory_in_bytes / (1024 * 1024)
        # Add more unit conversions here

    @staticmethod
    def _measure_performance(start_time, start_memory, elapsed, memory, name):
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
    