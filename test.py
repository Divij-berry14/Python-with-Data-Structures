class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def numberOfNodes(root):
    if root==None:
        return 0
    leftC=numberOfNodes(root.left)
    rightC=numberOfNodes(root.right)
    return 1+ leftC+rightC

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
printDetailTree(root)
print("Number of Nodes",numberOfNodes(root))
printPostOrder(root)
