class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes_ll(head, i, j):
    curr = head
    count = 0
    x = 0
    y = 0
    if i == j:
        return head
    while curr is not None:
        if count == i:
            x = curr.data
        elif count == j:
            y = curr.data
        curr = curr.next
        count += 1
    if x == y:
        return head

    prev_x = None
    curr_x = head
    while curr_x is not None and curr_x.data != x:
        prev_x = curr_x
        curr_x = curr_x.next

    prev_y = None
    curr_y = head
    while curr_y is not None and curr_y.data != y:
        prev_y = curr_y
        curr_y = curr_y.next

    if curr_x is None or curr_y is None:
        return head

    if prev_x is not None:
        prev_x.next = curr_y
    else:
        head = curr_y

    if prev_y is not None:
        prev_y.next = curr_x
    else:
        head = curr_x

    temp = curr_x.next
    curr_x.next = curr_y.next
    curr_y.next = temp
    return head


def print_ll(head):
    while head is not None:
        print(head.data, "->", end="")
        head = head.next
    print("None")


def input_ll():
    li_val = [int(i) for i in input().split()]
    head = None
    tail = None
    for curr_val in li_val:
        if curr_val is -1:
            break
        new_node = Node(curr_val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


Head = input_ll()
print_ll(Head)
Head = swap_nodes_ll(Head, 3, 4)
print_ll(Head)