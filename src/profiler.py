import os
import tempfile
import cProfile


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
