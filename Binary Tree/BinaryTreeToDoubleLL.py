class Node(object):
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def BTToDLLUtil(root):
    """This is a utility function to
    convert the binary tree to doubly
    linked list. Most of the core task
    is done by this function."""
    if root is None:
        print("None statement running")
        return root

    if root.left:
        print("left1")
        # Convert the left subtree
        left = BTToDLLUtil(root.left)
        print("left1", left.data)

        while left.right:
            print("left2")
            left = left.right

        print("data1", root.data)
        left.right = root
        print("left3")

        root.left = left


    if root.right:
        print("right1")
        # Convert the right subtree
        right = BTToDLLUtil(root.right)
        print("right1", right.data)

        while right.left:
            print("right2")
            right = right.left


        print("data2", root.data)
        right.left = root
        print("right3")

        root.right = right
    print("first")
    return root


def BTToDLL(root):
    if root is None:
        return root

    # Convert to doubly linked
    # list using BLLToDLLUtil
    root = BTToDLLUtil(root)

    # We need pointer to left most
    # node which is head of the
    # constructed Doubly Linked list
    while root.left:
        root = root.left

    return root


def print_list(head):

    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right


# if __name__ == '__main__':
#     root = Node(10)
#     root.left = Node(12)
#     root.right = Node(15)
#     root.left.left = Node(25)
#     root.left.right = Node(30)
#     root.right.left = Node(36)
#     root.right.right = Node(50)
#     head = BTToDLL(root)
#     print_list(head)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.right = Node(3)
    # root.right.left = Node(4)
    head = BTToDLL(root)
    print_list(head)

