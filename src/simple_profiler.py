import os
import pstats
import tempfile
import cProfile
from cStringIO import StringIO


class profile(object):
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def __call__(self, func):
        def _inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            return_value = func(*args, **kwargs)
            pr.disable()
            fd, stats_filename = tempfile.mkstemp(dir=self.output_dir)
            os.close(fd)
            pr.dump_stats(stats_filename)
            return return_value
        return _inner


def print_stats(commandline_args):
    stats_dir = commandline_args[1]
    stats_filenames = os.listdir(stats_dir)
    stats_filename = stats_filenames[0]
    stats_file_path = os.path.join(stats_dir, stats_filename)
    s = StringIO()
    ps = pstats.Stats(stats_file_path, stream=s)
    for stats_filename in stats_filenames[1:]:
        stats_file_path = os.path.join(stats_dir, stats_filename)
        ps.add(stats_file_path)
    sortby = 'cumulative'
    ps.sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
