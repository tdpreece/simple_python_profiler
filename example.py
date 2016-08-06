import time

from profiler import profile


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
