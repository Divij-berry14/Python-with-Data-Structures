class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle_ll(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def remove_cycle_ll(head):
    meet_node = detect_cycle_ll(head)
    curr = head
    while curr.next != meet_node.next:
        curr = curr.next
        meet_node = meet_node.next
    meet_node.next = None
    return head


def make_cycle_ll(head, pos):
    curr = head
    count = 1
    start_node = None
    while curr.next is not None:
        if count == pos:
            start_node = curr
        curr = curr.next
        count += 1
    curr.next = start_node
    return head


def print_ll(head):
    while head is not None:
        print(head.data, "->", end="")
        head = head.next
    print("None")


def input_ll():
    input_list = [int(i) for i in input().split()]
    head = None
    tail = None
    for i in input_list:
        if i is -1:
            break
        new_node = Node(i)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


Head = input_ll()
print_ll(Head)
Head = make_cycle_ll(Head, 3)
# print_ll(Head)
val = detect_cycle_ll(Head)
if val is None:
    print("False")
else:
    print("True")
Head = remove_cycle_ll(Head)
val = detect_cycle_ll(Head)
if val is None:
    print("False")
else:
    print("True")

