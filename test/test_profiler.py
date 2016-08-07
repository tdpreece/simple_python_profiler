import os
import tempfile
import shutil
from unittest import TestCase

from mock import MagicMock, sentinel

from simple_profiler import profile


class TestProfileDecorator(TestCase):
    def setUp(self):
        self.dir_path = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.dir_path))
        self.profiled_function = MagicMock(return_value=sentinel.return_value)
        self.profile_decorator = profile(self.dir_path)
        self.decorated_function = self.profile_decorator(
            self.profiled_function
        )

    def test_profiled_function_with_no_args_is_executed(self):
        self.decorated_function()
        self.profiled_function.assert_called_once_with()

    def test_profiled_function_with_args_is_executed(self):
        args = (sentinel.arg1, sentinel.arg2)
        self.decorated_function(*args)
        self.profiled_function.assert_called_once_with(*args)

    def test_profiled_function_with_kwargs_is_executed(self):
        kwargs = {
            'key1': sentinel.value1,
            'key2': sentinel.value2
        }
        self.decorated_function(**kwargs)
        self.profiled_function.assert_called_once_with(**kwargs)

    def test_returns_returned_variables_of_profiled_function(self):
        return_value = self.decorated_function()
        expected_return_value = self.profiled_function()
        self.assertEqual(return_value, expected_return_value)

    def test_one_stats_files_are_saved_for_one_calls_of_function(self):
        stats_files_before = os.listdir(self.dir_path)
        self.assertEqual(len(stats_files_before), 0)

        self.decorated_function()

        stats_files_after = os.listdir(self.dir_path)
        self.assertEqual(len(stats_files_after), 1)

    def test_two_stats_files_are_saved_for_two_calls_of_function(self):
        stats_files_before = os.listdir(self.dir_path)
        self.assertEqual(len(stats_files_before), 0)

        self.decorated_function()
        self.decorated_function()

        stats_files_after = os.listdir(self.dir_path)
        self.assertEqual(len(stats_files_after), 2)
