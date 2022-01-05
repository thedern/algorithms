
"""
Pre-Order Traversal:
Search order is root, then left-subtree, then right-subtree.  Left is completed first, before
any right is completed
Example, Root --> left of left-subtree, right of left-subtree, --> left of right-subtree, right of right-subtree
Example of use:  Copy a tree

In-Order Traversal:
Left --> Root --> Right

Post-Order Traversal:
Left --> Right --> Root
This visits leaves before nodes, starts at the bottom and works backwards toward root
Example of use is to delete leaf nodes from a tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_print(root, path=""):
    """
    nodes first
    root --> left --> right
    """
    if root:
        path += str(root.data) + '-'
        path = preorder_print(root.left, path)
        path = preorder_print(root.right, path)
    return path


def inorder_print(root, path=""):
    """
    leaves first
    left --> root --> right
    """
    if root:
        path = inorder_print(root.left, path)
        path += str(root.data) + '-'
        path = inorder_print(root.right, path)
    return path


def postorder_print(root, path=""):
    """
    Leaves first
    left --> right --> root
    """
    if root:
        path = postorder_print(root.left, path)
        path = postorder_print(root.right, path)
        path += str(root.data) + '-'
    return path


def main():
    # tree objects using 'Node' class
    root = Node("F")
    root.left = Node("D")   # node
    root.left.left = Node("B")  # node
    root.left.left.left = Node("A")  # leaf
    root.left.left.right = Node("C")  # leaf
    root.left.right = Node("E")  # leaf
    root.right = Node("I")  # node
    root.right.left = Node("G")  # node
    root.right.left.right = Node("H")  # leaf
    root.right.right = Node("J")  # leaf

    print("Preorder:", preorder_print(root))
    print("Inorder:", inorder_print(root))
    print("Postorder:", postorder_print(root))


if __name__ == '__main__':
    main()


"""
Tree Diagram
                F
        /--------------\
        D               I
     /-----\         /-----\
    B       E       G       J
  /-----\             \
 A       C             H


"""