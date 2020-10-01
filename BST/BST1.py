#BST are binary tree which is faster in searching.
#Everything on left is smaller than root and everthing on right greater than root
#Time complexity in BST in balanced and good BST is O(h), h-->Height of the Tree-->h=O(log(n))
#Time complexity in BST in worst case(when the nodes are on one side only) is O(n),
# n-->Number of nodes in the Tree.

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def BSTSearch(root, k):
    if root is None:
        return False
    if root.data == k:
        return True
    if k < root.data:
        return BSTSearch(root.left, k)
    else:
        return BSTSearch(root.right, k)

def printBST(root):
    if root is None:
        return None
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data, end="")
    print()
    printBST(root.left)
    printBST(root.right)

def LevelWiseInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while q.empty() is False:
        currentNode = q.get()
        print("Enter a left child of", currentNode.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        print("Enter right child of", currentNode.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root

root = LevelWiseInput()
printBST(root)
print(BSTSearch(root, 5))