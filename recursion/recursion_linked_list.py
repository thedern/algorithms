

class Node:
    def __init__(self, data, next_item=None):
        self.data = data
        self.next_item = next_item


# create instances

def traverse_list(head):
    if head is None:
        return

    # recursive case
    print(head.data)
    return traverse_list(head.next_item)


def main():
    item1 = Node('dog')
    item2 = Node('cat')
    item3 = Node('bat')

    # link
    item1.next_item = item2
    item2.next_item = item3

    # enter recursive traversal
    traverse_list(item1)


if __name__ == '__main__':
    main()


