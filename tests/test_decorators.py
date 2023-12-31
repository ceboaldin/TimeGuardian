import unittest
from unittest.mock import patch
from timeguardian.decorators import time_func
import time


class TestTimeFuncDecorator(unittest.TestCase):


    @patch('timeguardian.decorators.logger')
    def test_decorator_without_custom_name(self, mock_logger):
        @time_func
        def sample_function():
            return "test"

        result = sample_function()
        self.assertEqual(result, "test")
        self.assertTrue(mock_logger.info.called)


    @patch('timeguardian.decorators.logger')
    def test_decorator_with_custom_name(self, mock_logger):
        @time_func(name="CustomFunction")
        def another_function():
            return 42

        result = another_function()
        self.assertEqual(result, 42)
        mock_logger.info.assert_called_with(unittest.mock.ANY)  # Check if logger.info was called with any argument
    

    @patch('timeguardian.decorators.logger')
    def test_time_measurement(self, mock_logger):
        @time_func
        def delay_function():
            time.sleep(0.1)  # Introducing a small delay

        delay_function()
        args, _ = mock_logger.info.call_args
        self.assertTrue("Elapsed time:" in args[0])

