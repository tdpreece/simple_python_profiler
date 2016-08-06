from unittest import TestCase

from mock import MagicMock, sentinel

from profiler import profile


class TestProfileDecorator(TestCase):
    def test_profiled_function_with_no_args_is_executed(self):
        profiled_function = MagicMock()
        profile(profiled_function)()
        profiled_function.assert_called_once_with()

    def test_profiled_function_with_args_is_executed(self):
        profiled_function = MagicMock()
        args = (sentinel.arg1, sentinel.arg2)
        profile(profiled_function)(*args)
        profiled_function.assert_called_once_with(*args)

    def test_profiled_function_with_kwargs_is_executed(self):
        profiled_function = MagicMock()
        kwargs = {
            'key1': sentinel.value1,
            'key2': sentinel.value2
        }
        profile(profiled_function)(**kwargs)
        profiled_function.assert_called_once_with(**kwargs)

    # def test_stats_file_is_printed(self):
