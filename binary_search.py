"""
this program illustrates the power of a binary search versus a simple search.
Enter any number for 'lsMax' and then any number between 1 and lsMax in the function call.
The loop counter will tell you how many iterations it took to locate your number.
The results are truly impressive.  Page 9 in Grokking algorithms
"""

# create list
ls1 = []
counter = 1
lsMax = 1000
while counter <= lsMax:
    ls1.append(counter)
    counter += 1
print("list is {}".format(ls1))


def binary_search(ls, item):
    """

    :param list: list of possible numbers
    :type list: list
    :param item: number to search
    :type item: int
    :return:
    :rtype:
    """
    low = 0
    loop = 0
    print(f"item is {item}")
    # lists start at index 0, so len is len -1
    high = len(ls) - 1
    print(f"low index is: {low}")
    print(f"high index is: {high}")

    while low <= high:
        loop += 1
        print(f"loop {loop}")

        # floor division to round down
        mid = (low + high) // 2
        # set guess to the value of the mid index
        guess = ls[mid]
        print(f"guess is {guess}")

        if guess == item:
            return mid
        # if guess is greater than the number, reset the high index to the mid index - 1
        if guess > item:
            high = mid - 1
        # if guess is lower than the number, reset the low index to the mid index + 1
        else:
            low = mid + 1
    return None


def main():
    # enter any number between 1 and lsMax
    print(binary_search(ls1, 1000))


if __name__ == "__main__":
    main()
