import cProfile


class profile(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        return_value = self.func(*args, **kwargs)
        pr.disable()
        stats_file = 'stats'
        pr.dump_stats(stats_file)
        return return_value
