#%%
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def search(node,key): #here node means the node of a tree and key means the value we are looking for
    print("current node is", node.data)
    if node is None:
        return "Not found"
    if node.data == key:
        print("node found")
        return node
    if node.data > key :
        return search(node.left,key)
    return search(node.right, key)


"""
The below creation of the tree is to check if search function is working or not.
"""
tree = Node(8)
second_r = Node(10)
second_l= Node(5)
tree.right = second_r
tree.left = second_l
second_l.left = Node(2)
second_l.right = Node(6)
second_r.left = Node(9)
second_r.right = Node(15)

"""
              8
           /    \
          5      10
         / \     / \
        2   6   9   15

        preorder = [8 5 2 6 10 9 15]

"""
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
preorder(tree)
search(tree,5)