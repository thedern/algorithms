"""
this program illustrates the power of a binary search versus a simple search.
Enter any number for 'lsMax' and then any number between 1 and lsMax in the function call.  The loop counter will tell you how many iterations it took to locate your number. The results are truly impressive.  Page 9 in Grokking algoritms
"""

# create list
ls1 = []
counter = 1
lsMax = 1000
while counter <= lsMax:
    ls1.append(counter)
    counter += 1
print("list is {}".format(ls1))

# binary search


def binary_search(list, item):
    low = 0
    loop = 0
    print("item is {}".format(item))
    # lists start at idex 0, so len is len -1
    high = len(list) - 1
    print("high index is.{}".format(high))

    while low <= high:
        loop += 1
        print("loop {}".format(loop))

        # floor division to round down
        mid = (low + high) // 2
        print("mid index is {}".format(mid))
        guess = list[mid]
        print("guess is {}".format(guess))

        if guess == item:
            return mid
        # if guess is greater than the number, go down in index
        if guess > item:
            high = mid - 1
        # if guess is lower than the number, go up in index
        else:
            low = mid + 1
    return None


# enter any number between 1 and lsMax
print(binary_search(ls1, 31))
