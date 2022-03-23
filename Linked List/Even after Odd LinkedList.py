class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def odd_even_ll(head):
    if head is None:
        return head
    curr = head
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None
    while curr is not None:
        if curr.data % 2 != 0:
            if odd_head is None:
                odd_head = curr
                odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr
        else:
            if even_head is None:
                even_tail = curr
                even_head = curr
            else:
                even_tail.next = curr
                even_tail = curr
        curr = curr.next
    if odd_head is None:
        return even_head
    odd_tail.next = even_head
    return odd_head


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
Head = odd_even_ll(Head)
print_ll(Head)