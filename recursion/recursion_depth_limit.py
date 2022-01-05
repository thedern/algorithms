
import sys


def factorial(n):
    if n <= 1:
        # Base Case
        return 1
    return n * factorial(n - 1)


def set_recursion_limit(n):
    sys.setrecursionlimit(n)


def main():
    set_recursion_limit(1003)  # default is 1000
    print(sys.getrecursionlimit())
    print(factorial(1000))  # RecursionError: maximum recursion depth exceeded in comparison if not reset from default


if __name__ == '__main__':
    main()
