import queue

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def numberOfNodes(root):
    if root == None:
        return 0
    leftC = numberOfNodes(root.left)
    rightC = numberOfNodes(root.right)
    return 1+ leftC+rightC

def LargestNode(root):
    if root == None:
        return -1
    leftS = LargestNode(root.left)
    rightS = LargestNode(root.right)
    res = max(leftS, rightS, root.data)
    return res

def HeightTree(root):
    if root == None:
        return 0
    leftH=HeightTree(root.left)
    rightH=HeightTree(root.right)
    return max(leftH, rightH)+1

def NumofLeafNodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    leftS=NumofLeafNodes(root.left)
    rightS=NumofLeafNodes(root.right)
    return leftS + rightS

def PrintDepthK(root,k):
    if root==None:
        return
    if k==0:
        print(root.data)
        return
    PrintDepthK(root.left,k-1)
    PrintDepthK(root.right,k-1)

def NodesGreater(root,k):
    if root == None:
        return 0
    c = 0
    if root.data > k:
        c = c+1
    c = c+NodesGreater(root.left,k)
    c = c+NodesGreater(root.right,k)
    return c

def checkNodePresent(root,k):
    if root==None:
        return
    if root.data == k:
        return True
    if checkNodePresent(root.left, k):
        return True
    if checkNodePresent(root.right, k):
        return True
    return False

def NodeswithoutSibling(root):
    if root==None:
        return 0
    if root.left==None and root.right!=None:
        print(root.right.data)
        NodeswithoutSibling(root.right)
        return
    if root.left!=None and root.right==None:
        print(root.left.data)
        NodeswithoutSibling(root.left)
        return
    NodeswithoutSibling(root.left)
    NodeswithoutSibling(root.right)


def pathSum(root, sum):
    def path_a(root, sum):
        res = 0
        if root == None:
            return 0
        if root.data == sum:
            res += 1
        res = res + path_a(root.left, sum - root.data)
        res = res + path_a(root.right, sum - root.data)
        return res

    if root == None:
        return 0
    return pathSum(root.left, sum) + path_a(root, sum) + pathSum(root.right, sum)

def RemoveLeafNodes(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = RemoveLeafNodes(root.left)
    root.right = RemoveLeafNodes(root.right)
    return root

def MirrorBT(root):
    if root == None:
        return  None
    left = root.left
    root.left = root.right
    root.right = left
    MirrorBT(root.left)
    MirrorBT(root.right)
    return root

def CheckBalancedTree(root):
    if root == None:
        return True
    leftH = HeightTree(root.left)
    rightH = HeightTree(root.right)
    if abs(leftH-rightH) > 1:
        return False
    left = CheckBalancedTree(root.left)
    right = CheckBalancedTree(root.right)
    if left and right:
        return True
    else:
        return False

def CheckBalancedBTimproved(root):
    if root == None:
        return 0, True
    lh, isLeftBalanced = CheckBalancedBTimproved(root.left)
    rh, isRightBalanced = CheckBalancedBTimproved(root.right)
    h = 1 + max(lh, rh)
    if abs(lh-rh) > 1:
        return h, True
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        h, False

def DiameterBT(root):
    if root == None:
        return 0
    leftD = DiameterBT(root.left)
    rightD = DiameterBT(root.right)
    print(leftD,rightD)
    printDetailTree(root)
    d = HeightTree(root.left) + HeightTree(root.right)
    print("d", d)
    return max(leftD, rightD, d)

def MinimumDepth(root):
    if root == None:
        return 0
    # if root.left ==None and root.right ==None:
    #     return 1
    if root.left is None:
        return MinimumDepth(root.right)+1
    if root.right is None:
        return MinimumDepth(root.left)+1
    leftH = MinimumDepth(root.left)
    rightH = MinimumDepth(root.right)
    res = min(leftH, rightH)+1
    return res

def isUnivalTree(root):
    if root is None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left == None:
        if isUnivalTree(root.right) and root.right.data == root.data:
            return True
        else:
            return False
    if root.right == None:
        if isUnivalTree(root.left) and root.left.data == root.data:
            return True
        else:
            return False
    if root.data != root.left.data or root.data != root.right.data:
        return False
    left = isUnivalTree(root.left)
    right = isUnivalTree(root.right)
    if left and right:
        return True
    return False


# def BTToDLL(root,LLhead, prev):
#     if root == None:
#         return
#
#     BTToDLL(root.left, LLhead, prev)
#
#     if prev.data == 0:
#         print("if prev")
#         print(root.data)
#         LLhead = root
#         prev = root
#
#     else:
#         print("prev else")
#         print(root.data)
#         root.left = prev
#         prev.right = root
#         prev = root
#
#     BTToDLL(root.right, LLhead, prev)
#     # return LLhead
def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        currentNode = q.get()
        print("Enter left child of ", currentNode.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(currentNode.data)
            currentNode.left = leftChild
            q.put(leftChild)
        print("Enter right child of", currentNode.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root

def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printDetailTree(root):
    if root == None:
        return
    print(root.data, end =":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data, end="")
    print()
    printDetailTree(root.left)
    printDetailTree(root.right)

def printPostOrder(root):
    if root==None:
        return
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.data)

def InputTree():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = InputTree()
    rightTree = InputTree()
    root.left = leftTree
    root.right = rightTree
    return root

def print_LL(head):
    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right

# btn1 = BinaryTreeNode(1)
# btn2 = BinaryTreeNode(2)
# btn3 = BinaryTreeNode(3)
# btn4 = BinaryTreeNode(4)
#
# btn1.left = btn2
# btn1.right = btn3
# btn2.left = btn4
# printTree(btn1)
LLhead = Node(0)
prev = Node(0)
root = InputTree()
# printDetailTree(btn1)
# root = takeLevelWiseTreeInput()
# printDetailTree(root)
# head = BTToDLL(root, LLhead, prev)
# print_LL(head)
# print("Number of Nodes",numberOfNodes(root))
# # printPostOrder(root)
# print("largest Node",LargestNode(root))
# print("Height of the Tree",HeightTree(root))
# print("Number of Leaf Nodes in Binary Tree",NumofLeafNodes(root))
# PrintDepthK(root,2)
# print(NodesGreater(root,8))
# print(checkNodePresent(root,2))
# NodeswithoutSibling(root)
# root = MirrorBT(root)
# printDetailTree(root)
# print(CheckBalancedTree(root))
# print(CheckBalancedBTimproved(root))
# print(DiameterBT(root))
# print(MinimumDepth(root))
# print(isUnivalTree(root))

