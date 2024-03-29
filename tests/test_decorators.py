# test_decorators.py
import pytest
from unittest.mock import ANY
from unittest.mock import patch


def test_simple_function(simple_function, mocker):
    """
    Test case for the simple_function.

    Args:
        simple_function: The function to be tested.
        mocker: The mocker object for patching.

    Returns:
        None
    """
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = simple_function()
    assert result == "test"
    mock_logger.info.assert_called()


def test_delayed_function_with_custom_name(delayed_function, mocker):
    """
    Test case for the delayed_function with a custom name.

    Args:
        delayed_function: The delayed function to be tested.
        mocker: The mocker object for patching.

    Returns:
        None
    """
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = delayed_function()
    assert result == "done"
    mock_logger.info.assert_called_with(ANY)


def test_slow_function_logs_time(slow_function, mocker):
    """
    Test case to verify that the slow_function logs the time correctly.

    Args:
        slow_function: The slow function to be tested.
        mocker: The mocker object for patching.

    Returns:
        None
    """
    mock_logger = mocker.patch('timeguardian.decorators.logger')
    result = slow_function()
    assert result == "slow"
    mock_logger.info.assert_called_with(ANY)

@pytest.mark.asyncio
async def test_async_function(async_function):
    """
    Test case for an asynchronous function.

    Args:
        async_function: The async function to be tested.

    Returns:
        None
    """
    with patch('timeguardian.decorators.logger') as mock_logger:
        await async_function()
        mock_logger.info.assert_called_with(ANY)

def test_memory_logging(memory_intensive_function):
    """
    Test case to verify that the memory logging occurs correctly.

    Args:
        memory_intensive_function: The function to be tested.

    Returns:
        None
    """
    with patch('timeguardian.decorators.logger') as mock_logger:
        memory_intensive_function()
        mock_logger.info.assert_called()

def test_custom_name_logging(custom_named_function):
    """
    Test case to verify that logging with a custom name works.

    Args:
        custom_named_function: The function to be tested.

    Returns:
        None
    """
    with patch('timeguardian.decorators.logger') as mock_logger:
        custom_named_function()
        mock_logger.info.assert_called_with(ANY)



