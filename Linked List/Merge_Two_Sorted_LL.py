class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_ll(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data > head2.data:
        final_head = head2
        final_tail = head2
        head2 = head2.next
    else:
        final_head = head1
        final_tail = head1
        head1 = head1.next

    while head1 is not None and head2 is not None:
        if head1.data > head2.data:
            final_tail.next = head2
            final_tail = final_tail.next
            head2 = head2.next
        else:
            final_tail.next = head1
            final_tail = final_tail.next
            head1 = head1.next
    if head1 is not None:
        final_tail.next = head1
    if head2 is not None:
        final_tail.next = head2
    return final_head


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


Head1 = input_ll()
Head2 = input_ll()
print_ll(Head1)
print_ll(Head2)
Head = merge_sorted_ll(Head1, Head2)
print_ll(Head)