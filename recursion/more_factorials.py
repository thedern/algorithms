# compares a while loop with recursive function to achieve same results

def factorial_iterative_while(n):
    """
    Non-recursive function uses while loop
    """

    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result


def factorial_recursive(n):
    """
    recursive function for factorial
    """
    if n == 1:
        return n
    return n * factorial_recursive(n - 1)


def main():
    # factorial 4 (4!)  = 4 * 3 * 2 * 1

    try:
        assert factorial_iterative_while(4) == 24
    except AssertionError as e:
        print('incorrect assertion')

    try:
        assert factorial_recursive(4) == 24
    except AssertionError as e:
        print('incorrect assertion')

    # factorial = trace(factorial_recursive)
    # factorial(5)


if __name__ == "__main__":
    main()

