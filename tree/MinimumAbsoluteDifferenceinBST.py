# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        ans = float('inf')
        def inorder(root):
            nonlocal prev, ans
            if root is not None:
                inorder(root.left)
                if prev is not None:
                    ans = min(ans, abs(prev - root.val))
                prev = root.val
                inorder(root.right)
        inorder(root)
        return ans   


        
        
        
        