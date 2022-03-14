class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def palindrome_ll(head):
    if head is None:
        return True
    s = []
    while head is not None:
        s.append(head.data)
        head = head.next
    right = len(s) - 1
    left = 0
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True


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
print(palindrome_ll(Head))
