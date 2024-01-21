import pytest
from timeguardian.decorators import TimeGuardian
import asyncio

# Fixture for a simple function
@pytest.fixture
def simple_function():
    @TimeGuardian.measure
    def function():
        return "test"
    return function

# Fixture for a delayed function with custom name
@pytest.fixture
def delayed_function():
    @TimeGuardian.measure(name="CustomDelayedFunction")
    def function():
        # Some delay logic
        return "done"
    return function

# Fixture for a function that raises an exception
@pytest.fixture
def function_that_raises():
    @TimeGuardian.measure
    def function():
        raise ValueError("Error occurred")
    return function

# Fixture for a fast function
@pytest.fixture
def fast_function():
    @TimeGuardian.monitor(elapsed=200)  # Adjust the threshold as needed
    def function():
        # Logic for a fast execution
        return "fast"
    return function

# Fixture for a slow function (adjust as needed)
@pytest.fixture
def slow_function():
    @TimeGuardian.measure
    def function():
        # Logic for a slow execution
        return "slow"
    return function

# Fixture for an asynchronous function
@pytest.fixture
def async_function():
    @TimeGuardian.measure
    async def function():
        # Async logic
        return "async result"
    return function

# Fixture for a memory-intensive function
@pytest.fixture
def memory_intensive_function():
    @TimeGuardian.measure(memory=True)
    def function():
        # Memory intensive logic
        return "memory intensive"
    return function

# Fixture for a function with a custom name
@pytest.fixture
def custom_named_function():
    @TimeGuardian.measure(name="CustomName")
    def function():
        # Some logic
        return "custom named function"
    return function
