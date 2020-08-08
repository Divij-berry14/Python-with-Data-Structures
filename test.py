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
    c=0
    if root.data>k:
        c=c+1
    c=c+NodesGreater(root.left,k)
    c=c+NodesGreater(root.right,k)
    return c

def checkNodePresent(root,k):
    if root==None:
        return
    if root.data==k:
        return True
    if checkNodePresent(root.left,k):
        return True
    if checkNodePresent(root.right,k):
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
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=InputTree()
    rightTree=InputTree()
    root.left=leftTree
    root.right=rightTree
    return root


btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)

btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
# printTree(btn1)
root=InputTree()
# printDetailTree(btn1)
# printDetailTree(root)
# print("Number of Nodes",numberOfNodes(root))
# # printPostOrder(root)
# print("largest Node",LargestNode(root))
# print("Height of the Tree",HeightTree(root))
# print("Number of Leaf Nodes in Binary Tree",NumofLeafNodes(root))
# PrintDepthK(root,2)
# print(NodesGreater(root,8))
# print(checkNodePresent(root,2))
# NodeswithoutSibling(root)
print(pathSum(root,8))

