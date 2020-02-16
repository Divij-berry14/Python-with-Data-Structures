import queue
class Binary_Tree_Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def Binary_Search_Tree(root, k):
    if root==None:
        return False
    if root.data == k:
        return True
    if k < root.data:
        return Binary_Search_Tree(root.left, k)
    else:
        return Binary_Search_Tree(root.right, k)

def print_elements_range_BST(root,k1,k2):
    if root == None:
        return
    # if root.data>k1 and root.data<k2:
    #     print(root.data,sep=",")
    if root.data<k1:
        print_elements_range_BST(root.right, k1, k2)
    elif root.data>k2:
        print_elements_range_BST(root.left, k1, k2)
    else:
        print(root.data)
        print_elements_range_BST(root.left, k1, k2)
        print_elements_range_BST(root.right, k1, k2)

def level_wise_input():
    q=queue.Queue()
    print("Enter root")
    root_data = int(input())
    if root_data == -1:
        return None
    root = Binary_Tree_Node(root_data)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        left_child_data = int(input())
        if left_child_data != -1:
            left_child = Binary_Tree_Node(left_child_data)
            current_node.left = left_child
            q.put(left_child)

        print("Enter right child of", current_node.data)
        right_child_data = int(input())
        if right_child_data != -1:
            right_child = Binary_Tree_Node(right_child_data)
            current_node.right = right_child
            q.put(right_child)

    return root

def print_detailed_tree(root):
    if root==None:
        return None
    print(root.data, end=":")
    if root.left!=None:
        print("L", root.left.data, end=",")
    if root.right!= None:
        print("R", root.right.data, end="")
    print()
    print_detailed_tree(root.left)
    print_detailed_tree(root.right)

root = level_wise_input()
print_detailed_tree(root)
res=Binary_Search_Tree(root, 9)
print(res)
print_elements_range_BST(root, 5, 10)