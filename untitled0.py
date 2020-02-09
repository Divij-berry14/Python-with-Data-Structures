class Binary_Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def input_tree():
    rootData=int(input())
    if rootData==-1:
        return None
    root=Binary_Tree(rootData)
    leftTree=input_tree()
    rightTree=input_tree()
    root.left=leftTree
    root.right=rightTree
    return root

def num_nodes(root):
    if root==None:
        return 0
    left=num_nodes(root.left)
    right=num_nodes(root.right)
    return 1+left+right

def print_tree(root):
    if root==None:
        return
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)


def print_postOrder(root):
    if root==None:
        return 0
    if root.left!=None:
        print_postOrder(root.left)
    if root.right!=None:
        print_postOrder(root.right)
    return root.data
    
def print_detail_tree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    print_detail_tree(root.left)
    print_detail_tree(root.right)
    

bt1=Binary_Tree(1)
bt2=Binary_Tree(3)
bt3=Binary_Tree(4)
bt4=Binary_Tree(5)
bt5=Binary_Tree(6)
bt6=Binary_Tree(7)

bt1.left=bt2
bt1.right=bt3
bt3.right=bt4
bt3.left=bt5
bt2.left=bt6
root=input_tree()
#print_detail_tree(bt1)  
#print()
#print_detail_tree(root)
#print("Number of nodes",num_nodes(root))
print(print_postOrder(root))  
            