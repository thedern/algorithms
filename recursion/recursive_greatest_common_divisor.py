"""
Euclid's algorithm, continually subtract smaller from larger
GCD(a, b) == GCD(b, a - b)
example:  GCD(12, 8) == GCD(8, 12 - 8) == 4
example: GCD(32, 12) == GCD(12, 32 - 12) == GCD(20, 12)  == GCD(20, 20 - 12) == GCD(12, 8)  == GCD(12, 12 - 8) == 4
"""


def gcd_recursive(a, b):
    # testing for b == 0, protects against 'divide by zero error'.
    if b == 0:
        return a
    # call function with smaller number as larger num and remainder of mod div as smaller num
    return gcd_recursive(b, (a % b))


def main():
    print(gcd_recursive(4, 0))
    print(gcd_recursive(32, 12))
    print(gcd_recursive(50, 15))
    print(gcd_recursive(42, 28))
    print(gcd_recursive(28, 42))
    print(gcd_recursive(8, 2))
    print(gcd_recursive(16, 4))
    print(gcd_recursive(345, 766))


if __name__ == "__main__":
    main()
