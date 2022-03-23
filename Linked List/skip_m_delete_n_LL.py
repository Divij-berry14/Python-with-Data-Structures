class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skip_m_delete_n(head, m, n):
    if m == 0:
        return
    if head is None or n <= 0 or m <= 0:
        return head
    curr = head
    while curr is not None:
        for i in range(m-1):
            if curr is None:
                break
            curr = curr.next
        prev = curr
        curr = curr.next
        for i in range(n):
            if curr is None:
                break
            curr = curr.next
        prev.next = curr
        # prev = curr
        # curr = curr.next
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


Head = skip_m_delete_n(Head, 3, 2)
print_ll(Head)