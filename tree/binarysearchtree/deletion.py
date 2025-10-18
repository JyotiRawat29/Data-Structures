"""
still didnot understand the minimumValue()
"""
def minimumValue(node):
    while node.left is not None:
        node = node.left
    return node

def delete(node, key):
    if node is None:
        return None
    if node.data < key:
        node.right = delete(node.right,key)
    elif node.data > key:
        node.left = delete(node.left,key)
    else:
        #if the node has only one child(right side)
        if node.left is None:
            temp = node.right
            node = None
            return temp
        #if node has only one child(left side)
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        #if node has 2 children
        temp = minimumValue(node.right)#minimum of RST
        node.data = temp.data
        node.right = delete(node.right, temp.data) #why this line
    return node