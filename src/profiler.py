import os
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
            stats_file = os.path.join(self.output_dir, 'stats')
            pr.dump_stats(stats_file)
            return return_value
        return _inner
