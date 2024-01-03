# conftest.py
import pytest
from timeguardian.decorators import time_func
import time

@pytest.fixture
def simple_function():
    @time_func
    def function():
        return "test"
    return function

@pytest.fixture
def delayed_function():
    @time_func
    def function():
        time.sleep(0.1)
        return "done"
    return function

@pytest.fixture
def function_that_raises():
    @time_func
    def function():
        raise ValueError("Test Error")
    return function
