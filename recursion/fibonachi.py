

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        # range 0, n, includes lower, excludes upper
        # variable swap:  a = b, b = a + b
        a, b = b, a + b

    return a


def fibonacci_recursive(n):
    # base case
    if n < 2:
        return n
    # add two previous terms to get current term
    # decrements until n < 2
    # this is an expensive call algorithm as it loads up the call stack
    # (think about how fibonacci numbers work if one entered 10)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    # print(fibonacci_iterative(10))
    print(fibonacci_recursive(10))


if __name__ == "__main__":
    main()


