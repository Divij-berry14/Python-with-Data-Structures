import queue
class Binary_Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def num_nodes(root):
    if root==None:
        return 0
    left=num_nodes(root.left)
    right=num_nodes(root.right)
    return 1+left+right

def sum_nodes(root):
    if root==None:
        return 0
    left_sum=sum_nodes(root.left)
    right_sum=sum_nodes(root.right)
    return root.data+left_sum+right_sum

def largest_node(root):
    if root==None:
        return -1
    l_left=largest_node(root.left)
    l_right=largest_node(root.right)
    result=max(root.data,l_left,l_right)
    return result

def height_tree(root):
    if root==None:
        return 0
    left=height_tree(root.left)
    right=height_tree(root.right)
    return 1+max(left,right)

def leaf_nodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    left_n=leaf_nodes(root.left)
    right_n=leaf_nodes(root.right)
    return left_n+right_n

def depth_k(root,k):
    if root==None:
        return
    if k==0:
        print(root.data)
    depth_k(root.left,k-1)
    depth_k(root.right,k-1)
    

def depth_k_mod(root,k,d=0):
    if root==None:
        return 
    if d==k:
        print(root.data)
        return
    depth_k_mod(root.left,k,d+1)
    depth_k_mod(root.right,k,d+1)


def check_balanced(root):
    if root==None:
        return True
    left=height_tree(root.left)
    right=height_tree(root.right)
    if left-right>1 or right-left>1:
        return False
    is_L_balance=check_balanced(root.left)
    is_R_balance=check_balanced(root.right)
    if is_L_balance and is_R_balance:
        return True
    else:
        return False
    
def remove_leaf_nodes(root):
    if root==None:
        return 
    if root.left==None and root.right==None:
        return None
    root.left=remove_leaf_nodes(root.left)
    root.right=remove_leaf_nodes(root.right)
    return root

def diameter_tree(root):
    if root== None:
        return 0
    leftD=diameter_tree(root.left)
    rightD=diameter_tree(root.right)
    d=height_tree(root.left)+height_tree(root.right)
    return max(leftD,rightD,d)

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
    print(root.data)
    
def preOrder(root):
    if root==None:
        return 0
    print(root.data)
    if root.left!=None:
        preOrder(root.left)
    if root.right!=None:
        preOrder(root.right)
    
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

def level_wise_input():
    q=queue.Queue()
    print("Enter root")
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=Binary_Tree(rootdata)
    q.put(root)
    while(not(q.empty())):
        curr_node=q.get()
        print("Enter left child of",curr_node.data)
        left_data=int(input())
        if left_data!=-1:
            left_child=Binary_Tree(left_data)
            curr_node.left=left_child
            q.put(left_child)
        
        print("Enter right child of",curr_node.data)
        right_data=int(input())
        if right_data!=-1:
            right_child=Binary_Tree(right_data)
            curr_node.right=right_child
            q.put(right_child)
    
    return root

def print_level_wise_input(root):
    q=queue.Queue()
    q.put(root)
    while (not(q.empty())):
        curr_node=q.get()
        curr_data=curr_node.data
        left=-1
        right=-1
        if curr_node.left!=None:
            left=curr_node.left.data
            q.put(curr_node.left)
        if curr_node.right!=None:
            right=curr_node.right.data
            q.put(curr_node.right)
        
        print(curr_data,"L:",left,"R:",right)
#        else:
#            print("L",curr_node.left.data,end=",")
#            print("R",curr_node.right.data,end="")
        
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
#root=input_tree()
root=level_wise_input()
#print_detail_tree(root)
print_level_wise_input(root)
#print_detail_tree(bt1)  
#print()
#root=remove_leaf_nodes(root)
#print_detail_tree(root)
#print("Number of nodes",num_nodes(root))
#print("Post Order")
#print_postOrder(root)
#print("preOrder")
#preOrder(root)  
#print("sum of nodes",sum_nodes(root))
#print("Largest Node",largest_node(root))   
#print("Height Tree",height_tree(root))   
#print("No.of leaf nodes",num_nodes(root)) 
#depth_k(root,2)     
#depth_k_mod(root,2)
#remove_leaf_nodes(root)
#print("Is the Binary Tree balanced",check_balanced(root))
#print("Diameter of Tree is:",diameter_tree(root))