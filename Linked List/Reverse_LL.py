class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_ll_rec(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_rec(head.next)
    head.next.next = head
    head.next = None
    return small_head


def reverse_ll_rec_2(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_rec_2(head.next)
    curr = small_head
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return small_head


def reverse_ll_rec_3(head):
    if head is None or head.next is None:
        return head, head
    small_head, small_tail = reverse_ll_rec_3(head.next)
    small_tail.next = head
    head.next = None
    return small_head, head


def reverse_ll_rec_4(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_rec_4(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return small_head


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
Head = reverse_ll_rec(Head)
print_ll(Head)
Head = reverse_ll_rec_2(Head)
print_ll(Head)
Head, Tail = reverse_ll_rec_3(Head)
print_ll(Head)
Head = reverse_ll_rec_4(Head)
print_ll(Head)

