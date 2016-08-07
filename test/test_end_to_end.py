import os
import shutil
import subprocess
import tempfile
from unittest import TestCase

from mock import sentinel

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
        process = subprocess.Popen(
            ['print_stats', self.dir_path],
            stdout=subprocess.PIPE
        )
        stdout = process.communicate()[0]
        self.assertEqual(
            ret_val,
            sentinel.ret_val,
            msg='profile decorator not returning return value of function being profiled'
        )
        stdout_lines = stdout.split('\n')
        function1_stats = [line.strip() for line in stdout_lines if 'function1' in line][0]
        n_calls_function1 = [stat.strip() for stat in function1_stats.split('    ')][0]
        self.assertEqual(n_calls_function1, '2')


@profile(profile_results_dir)
def function1():
    function2()
    return sentinel.ret_val


def function2():
    pass
