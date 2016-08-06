import os
import tempfile
from unittest import expectedFailure, TestCase

from mock import MagicMock, sentinel

from profiler import profile


class TestProfileDecorator(TestCase):
    def setUp(self):
        self.profiled_function = MagicMock(return_value=sentinel.return_value)

    def test_profiled_function_with_no_args_is_executed(self):
        profile_decorator = profile()
        decorated_function = profile_decorator(self.profiled_function)
        decorated_function()
        self.profiled_function.assert_called_once_with()

    def test_profiled_function_with_args_is_executed(self):
        args = (sentinel.arg1, sentinel.arg2)
        profile_decorator = profile()
        decorated_function = profile_decorator(self.profiled_function)
        decorated_function(*args)
        self.profiled_function.assert_called_once_with(*args)

    def test_profiled_function_with_kwargs_is_executed(self):
        kwargs = {
            'key1': sentinel.value1,
            'key2': sentinel.value2
        }
        profile_decorator = profile()
        decorated_function = profile_decorator(self.profiled_function)
        decorated_function(**kwargs)
        self.profiled_function.assert_called_once_with(**kwargs)

    def test_returns_returned_variables_of_profiled_function(self):
        profile_decorator = profile()
        decorated_function = profile_decorator(self.profiled_function)
        return_value = decorated_function()
        expected_return_value = self.profiled_function()
        self.assertEqual(return_value, expected_return_value)

    @expectedFailure
    def test_stats_file_is_printed(self):
        dir_path = tempfile.mkdtemp()
        self.addCleanup(lambda: os.rmdir(dir_path))
        raise NotImplementedError()
