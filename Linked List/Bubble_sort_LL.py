class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length_ll(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count


def bubble_sort_ll(head):
    n = length_ll(head)
    for i in range(n-1):
        curr = head
        prev = None
        for j in range(n - i - 1):
            if curr.data <= curr.next.data:
                prev = curr
                curr = curr.next
            else:
                if prev is None:
                    fwd = curr.next
                    head = head.next
                    curr.next = fwd.next
                    fwd.next = curr
                    prev = fwd
                else:
                    fwd = curr.next
                    prev.next = fwd
                    curr.next = fwd.next
                    fwd.next = curr
                    prev = fwd
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
Head = bubble_sort_ll(Head)
print_ll(Head)