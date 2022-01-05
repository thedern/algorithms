
"""
memoization is the caching of calls/values in order not to duplicate work.
recursive calls have a lot of duplicate statements by definition.  lru cache can reuse previous calls reducing expensive
I/O bound computation.
"""
from functools import lru_cache


@lru_cache
def fin(n):
    """
     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
     function returns the n-th fibonacci number
    """
    if n in [0, 1]:
        return n
    return fin(n - 1) + fin(n - 2)


def main():
    # code takes around 1 second to run with lru_cache, and around 1 min w/o it
    print(fin(40))


if __name__ == '__main__':
    main()

