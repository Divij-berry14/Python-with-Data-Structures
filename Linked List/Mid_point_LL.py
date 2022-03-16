class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_ll(head):
    count = 0
    while head is not None:
        count = count+1
        head = head.next
    return count


def mid_point_ll(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    print(str(slow.data))
    # length = length_ll(head) - 1
    # count = 0
    # while head is not None:
    #     if count == length//2:
    #         print(head.data)
    #         break
    #     head = head.next
    #     count += 1


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
mid_point_ll(Head)