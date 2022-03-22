class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def linear_search_recursive(head, n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    temp = linear_search_recursive(head.next, n)
    if temp == -1:
        return -1
    return temp + 1


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
print(linear_search_recursive(Head, -34))

