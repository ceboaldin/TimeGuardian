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

@pytest.fixture
def fast_function():
    @TimeGuardian.measure(logTimeLimit=200)
    def function():
        time.sleep(0.05)  # 50ms, under the logTimeLimit
        return "fast"
    return function

@pytest.fixture
def slow_function():
    @TimeGuardian.measure(logTimeLimit=200)
    def function():
        time.sleep(0.3)  # 300ms, over the logTimeLimit
        return "slow"
    return function