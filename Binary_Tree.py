import queue
class Binary_Tree_Node():
    def __init__(self,data):
        self.data=data
        self.leftC=None
        self.rightC=None
        

def Build_Tree_from_PreOrder_Inorder(preOrder,inOrder):
    if len(preOrder)==0:
        return None
    rootData=preOrder[0]
    root=Binary_Tree_Node(rootData)
    root_Index_Inorder=-1
    for i in range(0,len(inOrder)):
        if inOrder[i]==rootData:
            root_Index_Inorder=i
            break
    if root_Index_Inorder==-1:
        return None
    leftInorder=inOrder[0:root_Index_Inorder]
    rightInorder=inOrder[root_Index_Inorder+1:]

    lenLeftSubtree=len(leftInorder)
    leftPreOrder=preOrder[1:lenLeftSubtree+1]
    rightPreOrder=preOrder[lenLeftSubtree+1:]

    leftChild=Build_Tree_from_PreOrder_Inorder(leftPreOrder,leftInorder)
    rightChild=Build_Tree_from_PreOrder_Inorder(rightPreOrder,rightInorder)
    root.leftC=leftChild
    root.rightC=rightChild
    return root

def level_wise_input():
    q=queue.Queue()
    print("Enter root")
    root_data=int(input())
    if root_data==-1:
        return None
    root=Binary_Tree_Node(root_data)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        left_child_data=int(input())
        if left_child_data!=-1:
            left_child=Binary_Tree_Node(left_child_data)
            current_node.leftC=left_child
            q.put(left_child)

        print("Enter right child of",current_node.data)
        right_child_data=int(input())
        if right_child_data!=-1:
            right_child=Binary_Tree_Node(right_child_data)
            current_node.rightC=right_child
            q.put(right_child)

    return root


def print_level_wise_input(root):
    q = queue.Queue()
    q.put(root)
    while (not (q.empty())):
        curr_node = q.get()
        curr_data = curr_node.data
        left = -1
        right = -1
        if curr_node.leftC != None:
            left = curr_node.leftC.data
            q.put(curr_node.leftC)
        if curr_node.rightC != None:
            right = curr_node.rightC.data
            q.put(curr_node.rightC)

        print(curr_data, "L:", left, "R:", right)


def print_Detailed_Tree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.leftC!=None:
        print("L",root.leftC.data,end=',')
    if root.rightC!=None:
        print("R",root.rightC.data,end='')
    print()
    print_Detailed_Tree(root.leftC)
    print_Detailed_Tree(root.rightC)

def Tree_input():                         #USER_INPUT
    rootData=int(input())
    if rootData==-1:
        return None
    root=Binary_Tree_Node(rootData)
    leftTree=Tree_input()
    rightTree=Tree_input()
    root.leftC=leftTree
    root.rightC=rightTree
    return root

def num_Nodes(root):
    if root==None:
        return 0
    leftCount=num_Nodes(root.leftC)
    rightCount=num_Nodes(root.rightC)
    return 1+leftCount+rightCount

def Largest_Node(root):
    if root==None:
        return -1
    leftLargest=Largest_Node(root.leftC)
    rightLargest=Largest_Node(root.rightC)
    largest=max(leftLargest,rightLargest,root.data)
    return largest

def countNodesGreaterThanX(root, x):
    if root==None:
        return 0
    result=0
    if root.data > x:
        result+=1
    result=result+countNodesGreaterThanX(root.leftC, x)
    result=result+countNodesGreaterThanX(root.rightC, x)
    return result

def height(root):
    if root==None:
        return 0
    leftTree=height(root.leftC)
    rightTree=height(root.rightC)
    number=max(leftTree,rightTree)
    return number+1

def number_of_leaf_Nodes(root):
    if root is None:
        return 0
    if root.leftC==None and root.rightC==None:
        return 1
    numLeftTree=number_of_leaf_Nodes(root.leftC)
    numRightTree=number_of_leaf_Nodes(root.rightC)
    return numLeftTree+numRightTree

def print_Nodes_At_DepthK(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
        return
    print_Nodes_At_DepthK(root.leftC,k-1)
    print_Nodes_At_DepthK(root.rightC,k-1)

def print_Nodes_At_DepthK_V2(root,k,depth=0):
    if root==None:
        return
    if k==depth:
        print(root.data)
        return
    print_Nodes_At_DepthK_V2(root.leftC,k,depth+1)
    print_Nodes_At_DepthK_V2(root.rightC,k,depth+1)

def Remove_Leaf_Nodes(root):
    if root==None:
        return None
    if root.leftC==None and root.rightC==None:
        return None
    root.leftC=Remove_Leaf_Nodes(root.leftC)
    root.rightC=Remove_Leaf_Nodes(root.rightC)
    return root

def is_Balanced(root):
    if root==None:
        return True
    left_height=height(root.leftC)
    right_height=height(root.rightC)
    if left_height - right_height>1 or right_height - left_height>1:
        return False
    is_left_Balanced=is_Balanced(root.leftC)
    is_right_Balanced=is_Balanced(root.rightC)
    if is_left_Balanced and is_right_Balanced:
        return True
    else:
        return False

def getHeight_and_CheckBalanced(root):
    if root==None:
        return 0,True
    lh,is_left_balanced=getHeight_and_CheckBalanced(root.leftC)
    rh,is_right_balanced=getHeight_and_CheckBalanced(root.rightC)

    h=1+max(lh,rh)

    if lh-rh>1 and rh-lh>1:
        return h,False

    if is_left_balanced and is_right_balanced:
        return h,True
    else:
        return h,False

def diameter_tree(root):
    if root== None:
        return 0
    leftD=diameter_tree(root.left)
    rightD=diameter_tree(root.right)
    d=height(root.left)+height(root.right)
    return max(leftD,rightD,d)



bt1=Binary_Tree_Node(1)
bt2=Binary_Tree_Node(4)
bt3=Binary_Tree_Node(5)
bt4=Binary_Tree_Node(3)
bt5=Binary_Tree_Node(6)
bt6=Binary_Tree_Node(7)
bt1.leftC=bt2
bt1.rightC=bt3
bt2.leftC=bt4
bt3.leftC=bt5
bt4.leftC=bt6
print("Detailed Binary Tree:")
print_Detailed_Tree(bt1)

root=Tree_input()
print_Detailed_Tree(root)

print("Number of nodes in Binary Tree are",num_Nodes(root))

print("Largest node in the Binary Tree",Largest_Node(root))

print("Nodes greater than x",countNodesGreaterThanX(root,4))

print("Height of the Tree",height(root))

print("Number of leaf Nodes:",number_of_leaf_Nodes(root))

print("Print number of nodes at depth k:",print_Nodes_At_DepthK(root,2))

print("Print number of nodes at depth k:",print_Nodes_At_DepthK_V2(root,2))

new_root=Remove_Leaf_Nodes(root)
print("After removal of leaf nodes, Binary Tree is:")
print_Detailed_Tree(new_root)

check=is_Balanced(root)
print("To check if the Binary Tree is Balanced or not:",is_Balanced(root))

print("To check if the Binary Tree is Balanced or not and Height of the Bianry Tree/Improved Version:",getHeight_and_CheckBalanced(root))

root=level_wise_input()
print_level_wise_input(root)

preOrder=[1,2,4,5,3,6,7]
inOrder=[4,2,5,1,6,3,7]
root=Build_Tree_from_PreOrder_Inorder(preOrder,inOrder)
print_Detailed_Tree(root)