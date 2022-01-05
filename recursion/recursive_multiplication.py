

"""
perform 'multiplication' by recursive division
example:  3 x 3 ==  3 + 3 + 3
example:  4 x 5 ==  5 + 5 + 5 + 5
"""


def recursive_multiplication(n, b):
    # negative n (which is the number of times we address the multiplicant, b)
    if n < 0:
        n, b = b, n
    # return 0 for if is 0
    if n == 0:
        return 0
    # return b if n is 1
    if n == 1:
        return b
    return b + recursive_multiplication((n - 1), b)


def main():
    print(recursive_multiplication(0, 12))
    print(recursive_multiplication(3, 0))
    print(recursive_multiplication(3, 3))
    print(recursive_multiplication(4, 3))
    print(recursive_multiplication(3, -3))
    print(recursive_multiplication(-3, 3))
    print(recursive_multiplication(0, 3))
    print(recursive_multiplication(1, 3))


if __name__ == '__main__':
    main()
