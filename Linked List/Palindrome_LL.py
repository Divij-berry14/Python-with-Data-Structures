class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def palindrome_ll_list(head):
    # O(n) space is used

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


def middle_node(head):
    slow = head
    fast = head
    while fast.next.next is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_node(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def palindrome_ll(head):
    # Without use of O(n) space
    if head is None:
        return None
    mid_node = middle_node(head)
    curr = head
    reverse_head = reverse_node(mid_node.next)
    while reverse_head is not None:
        if curr.data != reverse_head.data:
            return False
        else:
            curr = curr.next
            reverse_head = reverse_head.next
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
# print(palindrome_ll_list(Head))
print(palindrome_ll(Head))