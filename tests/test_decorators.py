import unittest
from unittest.mock import patch
from timeguardian.decorators import time_func
import time

# Test suite for the time_func decorator in the timeguardian.decorators module.
class TestTimeFuncDecorator(unittest.TestCase):

    # Test the time_func decorator when applied without a custom name.
    # This test checks if the decorator correctly logs the execution time
    # and ensures that the function's return value is not altered.
    @patch('timeguardian.decorators.logger')
    def test_decorator_without_custom_name(self, mock_logger):
        # Function decorated with time_func
        @time_func
        def sample_function():
            return "test"

        # Call the decorated function and check return value
        result = sample_function()
        self.assertEqual(result, "test")  # Verify return value remains unchanged

        # Verify if logger.info was called, indicating logging occurred
        self.assertTrue(mock_logger.info.called)

    # Test the time_func decorator with a custom name provided.
    # This test verifies if the custom name is correctly used in the log message.
    @patch('timeguardian.decorators.logger')
    def test_decorator_with_custom_name(self, mock_logger):
        # Function decorated with time_func and a custom name
        @time_func(name="CustomFunction")
        def another_function():
            return 42

        # Call the decorated function and check return value
        result = another_function()
        self.assertEqual(result, 42)  # Verify return value remains unchanged

        # Check if logger.info was called with any argument
        mock_logger.info.assert_called_with(unittest.mock.ANY)  

    # Test to verify the actual time measurement functionality of the decorator.
    # This test checks if the logging includes a mention of elapsed time.
    @patch('timeguardian.decorators.logger')
    def test_time_measurement(self, mock_logger):
        # Function decorated with time_func, including a deliberate delay
        @time_func
        def delay_function():
            time.sleep(0.1)  # Introducing a small delay

        # Call the decorated function
        delay_function()

        # Extract the logged message and verify it includes elapsed time info
        args, _ = mock_logger.info.call_args
        self.assertTrue("Elapsed time:" in args[0])  # Check for elapsed time in log
