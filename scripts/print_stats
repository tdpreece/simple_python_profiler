from cStringIO import StringIO
import pstats


def main():
    stats_file = 'stats'
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(stats_file, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()


if __name__ == '__main__':
    main()
