"""
selection sort O(n**2)
"""


def find_smallest(arr):
    """
    index 0 and value 0 are set as our initial smallest_value and smallest_index
    range over the length of the arr starting at index 1 and begin comparisons to smallest_value
    reset smallest_value as necessary

    :param arr: array of items
    :type arr: list
    :return: index of smallest item
    :rtype: int
    """
    smallest_value = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr1):
    """
    list comprehension:
    for as many indexes in the arr1, call find_smallest sending arr1 as argument
    append the value of the next smallest_index to the new_array, popping the value off arr1 each time
    due to arr1.pop(smallest), arr1 gets shorter/smaller with each loop taking less time to find next smallest

    :param arr1: array of items
    :type arr1: list
    :return: sorted array
    :rtype: list
    """

    return [arr1.pop(find_smallest(arr1)) for _ in range(len(arr1))]


def main(a):
    print(selection_sort(a))


if __name__ == '__main__':
    main([5, 3, 6, 2, 10, 1, 71, 16, 8])
