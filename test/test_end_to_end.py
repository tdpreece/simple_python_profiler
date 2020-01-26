import os
import shutil
import subprocess
from unittest import TestCase
from unittest.mock import sentinel

from simple_profiler import profile


this_dir = os.path.dirname(os.path.realpath(__file__))
profile_results_dir = os.path.join(this_dir, 'profile_results')


class TestEndToEnd(TestCase):
    longMessage = True

    def setUp(self):
        self.dir_path = profile_results_dir
        if os.path.exists(self.dir_path):
            shutil.rmtree(self.dir_path)
        os.mkdir(self.dir_path)
        self.addCleanup(lambda: shutil.rmtree(self.dir_path))

    def test_prints_stats_after_profiling_a_function(self):
        ret_val = function1()
        function1()
        stdout = self.print_profile_stats(self.dir_path)

        self.assertEqual(
            ret_val,
            sentinel.ret_val,
            msg='profile decorator not returning return value of function being profiled'
        )
        stats_output = StatsOutput(stdout)
        self.assertEqual(
            stats_output.get_n_calls('function1'),
            '2'
        )

    def print_profile_stats(self, dir_path):
        process = subprocess.Popen(
            ['print_profile_stats', dir_path],
            stdout=subprocess.PIPE
        )
        stdout = process.communicate()[0]
        return stdout


class StatsOutput(object):
    def __init__(self, stdout):
        self.stdout_lines = stdout.decode('utf-8').splitlines()

    def get_n_calls(self, function_name):
        function_stats = self.get_stats(function_name)
        n_calls_function1 = [stat.strip() for stat in function_stats.split('    ')][0]
        return n_calls_function1

    def get_stats(self, function_name):
        return [line.strip() for line in self.stdout_lines if function_name in line][0]


@profile(profile_results_dir)
def function1():
    function2()
    return sentinel.ret_val


def function2():
    pass
