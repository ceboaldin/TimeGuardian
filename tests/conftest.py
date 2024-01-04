# conftest.py
import pytest
from timeguardian.decorators import TimeGuardian
import time

@pytest.fixture
def simple_function():
    @TimeGuardian.measure
    def function():
        return "test"
    return function

@pytest.fixture
def delayed_function():
    @TimeGuardian.measure
    def function():
        time.sleep(0.1)
        return "done"
    return function

@pytest.fixture
def function_that_raises():
    @TimeGuardian.measure
    def function():
        raise ValueError("Test Error")
    return function