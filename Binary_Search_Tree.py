import queue
class Binary_Tree_Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# class BST:
#     def __init__(self):
#         self.root=None
#         self.numNodes=0
#
#     def print_Tree_Helper(self,root):
#         if root == None:
#             return None
#         print(root.data, end=":")
#         if root.left != None:
#             print("L",root.left.data, end=",")
#         if root.right != None:
#             print("R", root.right.data, end="")
#         self.print_Tree_Helper(self.left)
#         self.print_Tree_Helper(self.right)
#
#     def print_Tree(self):
#         return self.print_Tree_Helper(self.root)
#
#     def isPresentHelper(self, root, data):
#         if root == None:
#             return False
#         if root.data == data:
#             return True
#         if root.data > data:
#             return self.isPresentHelper(root.left, data)
#         else:
#             return self.isPresentHelper(root.right, data)
#
#     def isPresent(self, data):
#         return self.isPresentHelper(self.root, data)
#
#     def insert_Helper(self, root, data):
#         if root == None:
#             node = Binary_Tree_Node(data)
#             return node
#         if root.data > data:
#             root.left = self.insert_Helper(root.left, data)
#             return root
#         else:
#             root.right = self.insert_Helper(root.right, data)
#             return root
#
#     def insert(self, data):
#         self.numNodes = self.numNodes+1
#         self.root = self.insert_Helper(self)
#
#     def delete_data(self,data):
#
#     def count(self):
#         return 0

def Binary_Search_Tree (root, k):
    if root == None:
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

def Sorted_Array_to_Binary_Search_Tree(arr):
    l = len(arr)
    if l <= 0 or arr == None:
        return None
    root_index = (l-1)//2
    root = Binary_Tree_Node(arr[root_index])
    root.left = Sorted_Array_to_Binary_Search_Tree(arr[:root_index])
    root.right = Sorted_Array_to_Binary_Search_Tree(arr[root_index+1:])
    return root

def min_Tree(root):
    if root==None:
        return 10000
    leftMin=min_Tree(root.left)
    rightMin=min_Tree(root.right)
    return min(leftMin,rightMin,root.data)

def max_Tree(root):
    if root==None:
        return -110000
    leftMax = max_Tree(root.left)
    rightMax = max_Tree(root.right)
    return max(leftMax, rightMax, root.data)

def check_BST(root):
    if root==None:
        return True
    leftMax = max_Tree(root.left)
    rightMin = min_Tree(root.right)
    if root.data > rightMin or root.data <= leftMax:
        return False
    isLeftBST = check_BST(root.left)
    isrightBST = check_BST(root.right)
    return isLeftBST and isrightBST

def check_BST2(root):
    if root == None:
        return 100000, -100000, True
    leftMin, leftMax, is_left_BST= check_BST2(root.left)
    rightMin, rightMAx, is_right_BST= check_BST2(root.right)
    minimum= min(leftMin, rightMin, root.data)
    maximum= max(leftMax, rightMAx, root.data)
    is_tree_BST=True
    if root.data <= leftMax or root.data > rightMin:
        is_tree_BST = False
    if not(is_left_BST) or not(is_right_BST):
        is_tree_BST = False
    return minimum, maximum, is_tree_BST


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
        print("Enter left child of", current_node.data)
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
# res=Binary_Search_Tree(root, 9)
# print(res)
# print_elements_range_BST(root, 5, 10)
# print("Enter Sorted array")
# arr = [int(x) for x in input().split()]
# root = Sorted_Array_to_Binary_Search_Tree(arr)
# print_detailed_tree(root)
print(check_BST(root))
# print(check_BST2(root))

