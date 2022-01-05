
class Stack:
    """
    stacks are LIFO (Last in first out)
    """
    def __init__(self):
        """
        uses a python list to implement an example of a call 'stack'
        """
        self.items = []

    def is_empty(self):
        """
        checks if empty

        :return: true/false
        :rtype: bool
        """
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        """
        removes the last item from the list which is same as popping an item off the stack
        :return: none
        :rtype: none
        """
        return self.items.pop()

    def peek(self):
        """
        returns the top item in the stack (last item in the list)
        note:  does not remove item

        :return: item
        :rtype: any
        """
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items
