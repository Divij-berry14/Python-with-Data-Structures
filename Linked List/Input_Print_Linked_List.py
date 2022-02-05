class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):
    while head is not None:
        print(str(head.data) + "->", end="")
        head = head.next
    print("None")
    return


def take_input():
    head = None
    input_list = [int(x) for x in input().split()]
    for currData in input_list:
        if currData == -1:
            break
        new_node = Node(currData)
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    return head


Head = take_input()
print_ll(Head)
