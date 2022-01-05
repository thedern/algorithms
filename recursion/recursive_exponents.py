"""
exponents is just multiplication
3 ** 3 == 3 x 3 x 3
4 ** 3 == 4 x 4 x 4
"""


def recursive_exponents(b, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return b
    return b * recursive_exponents(b, (exp - 1))


def main():
    print(recursive_exponents(3, 0))
    print(recursive_exponents(3, 1))
    print(recursive_exponents(3, 2))
    print(recursive_exponents(3, 3))
    print(recursive_exponents(4, 2))
    print(recursive_exponents(2, 5))


if __name__ == "__main__":
    main()
