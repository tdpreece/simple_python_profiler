import cProfile
import time


def profile(func):
    def _inner():
        pr = cProfile.Profile()
        pr.enable()
        func()
        pr.disable()
        stats_file = 'stats'
        pr.dump_stats(stats_file)
    return _inner


def a_function():
    time.sleep(0.1)


def another_function():
    time.sleep(0.1)


@profile
def an_example():
    for i in range(3):
        a_function()
    for j in range(2):
        another_function()


if __name__ == '__main__':
    an_example()
