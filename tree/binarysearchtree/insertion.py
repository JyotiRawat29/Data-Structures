#%%
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    

def insert(root,node): #both arguments would be of class Node type
    if (root is None):
       root = node
       return
    if (root.data < node.data):
        if root.right == None :
            root.right = node
        else:
           insert(root.right,node)
    else:
       if root.left ==None:
          root.left = node
       else:
          insert(root.left,node)
        

#tree(Node(10,Node(8)))

"""
            10
           /  \    
          8    15
               / \
              12  16
             /      \
            11      18

            preorder[10 8 15 12 11 16 18]
"""
tree = Node(10)
insert(tree, Node(8))
insert(tree, Node(15))
insert(tree, Node(12))
insert(tree, Node(16))
#insert(tree, Node(15)) # there cannot be duplicate element in the BST
insert(tree, Node(18))
insert(tree, Node(11))


# %%
"""
in order to check the order in which the data is been fed to binary tree,
we have traversal methods: preorder, postorder and inorder. We can use one of the method to chcek. 
"""

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left) 
        preorder(root.right) 

#preorder(Node(8))
preorder(tree)
# %%
"""
            5
           / \
          3   7  
         / \  / \ 
        2   4 6  8
        [5 3 2 4 7 6 8]
"""
tree1 = Node(5)
insert(tree1, Node(3))
insert(tree1, Node(7))
insert(tree1, Node(2))
insert(tree1, Node(4))
insert(tree1, Node(6))
insert(tree1, Node(8))
preorder(tree1)
# %%
