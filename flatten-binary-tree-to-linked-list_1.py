# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        node = root
        while not node is None:
            if not node.right is None:
                stack.append(node.right)
            node.right = node.left
            node.left = None
            
            if node.right is None:
                if len(stack) == 0:
                    break
                else:
                    node.right = stack.pop()
                
            node = node.right