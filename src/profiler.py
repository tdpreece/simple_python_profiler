import cProfile


def profile(func):
    def _inner(*args):
        pr = cProfile.Profile()
        pr.enable()
        func(*args)
        pr.disable()
        stats_file = 'stats'
        pr.dump_stats(stats_file)
    return _inner
