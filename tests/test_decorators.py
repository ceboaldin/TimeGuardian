# test_decorators.py
import pytest
from unittest.mock import ANY

def test_simple_function(simple_function, mocker):
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = simple_function()
    assert result == "test"
    mock_logger.info.assert_called()

def test_delayed_function_with_custom_name(delayed_function, mocker):
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = delayed_function()
    assert result == "done"
    mock_logger.info.assert_called_with(ANY)

def test_decorator_with_exception(function_that_raises, mocker):
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    with pytest.raises(ValueError):
        function_that_raises()
    mock_logger.error.assert_called_with(ANY)

def test_fast_function_logs_nothing(fast_function, mocker):
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = fast_function()
    assert result == "fast"
    mock_logger.info.assert_not_called()

def test_slow_function_logs_time(slow_function, mocker):
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = slow_function()
    assert result == "slow"
    mock_logger.info.assert_called_with(ANY)