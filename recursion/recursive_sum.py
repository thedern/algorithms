

def list_sum(ls):

    """
    # long form...
    result = 0
    for item in ls:
        result += item
    return item

    """
    return sum(ls)


def list_sum_recursive(ls):
    """
    for each iteration of the function, ls[0] advances 1 index position to the right
    this repeats until the list is exhausted and then the call stack unwinds, returning the total
    """
    if not ls:
        return 0
    # passes in list from index 1, to the end back into list_sum_recursive
    return ls[0] + list_sum_recursive(ls[1:])


def main():
    assert list_sum([2, 3, 5, 7]) == 17
    assert list_sum_recursive([2, 3, 5, 7]) == 17


if __name__ == "__main__":
    main()
