import cProfile
import time


def a_function():
    time.sleep(1)


def another_function():
    time.sleep(1)


def an_example():
    profiler = cProfile.Profile()
    profiler.enable()

    for i in range(2):
        a_function()
    for j in range(2):
        another_function()

    profiler.disable()
    stats_file = 'stats'
    profiler.dump_stats(stats_file)


if __name__ == '__main__':
    an_example()
