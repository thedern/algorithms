"""
Divide and Conquer
if 0 elements, return empty list
1 element, return that 1 element in a list
create 3 lists (less then pivot, equal to pivot, greater than pivot)
join resulting 3 lists
"""


def quicksort(ls1):
    # find midpoint of list, list begins with index 0
    if len(ls1) <= 1:
        return ls1
    # pivot is the value of the middle index ls1[index]
    pivot = ls1[len(ls1) // 2]
    left = [x for x in ls1 if x < pivot]
    middle = [x for x in ls1 if x == pivot]
    right = [x for x in ls1 if x > pivot]
    # recursively quicksort left and right to get final sort
    return quicksort(left) + middle + quicksort(right)


def main():
    print(quicksort([5, 2, 6, 1]))
    print(quicksort([78, 2, 38, 72, 4 , 32, 1, 34, 499, 8]))


if __name__ == '__main__':
    main()