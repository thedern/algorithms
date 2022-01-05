

"""
get the length of a string using recursive addition
normally, we can just use the len() method
"""


def recursive_string(s):
    if not s:
        return 0
    return 1 + recursive_string(s[1:])


def main():
    print(recursive_string('darren smith'))


if __name__ == "__main__":
    main()
