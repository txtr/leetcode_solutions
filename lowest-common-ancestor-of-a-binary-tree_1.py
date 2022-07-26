# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertToBidirectional(self, node: 'TreeNode'):
        if node.left is not None:
            node.left.parent = node
            self.convertToBidirectional(node.left)
        if node.right is not None:
            node.right.parent = node
            self.convertToBidirectional(node.right)
        # uses O(nodes) aditional space
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.convertToBidirectional(root)
        
        ancestors_1 = []
        node_1 = p
        
        ancestors_1.append(node_1)
        while node_1 is not root:
            node_1 = node_1.parent
            ancestors_1.append(node_1)
        
        ancestors_2 = []
        node_2 = q
        
        ancestors_2.append(node_2)
        while node_2 is not root:
            node_2 = node_2.parent
            ancestors_2.append(node_2)
        
        LCA = 0 # dummy value
        
        x = -1
        try:
            while ancestors_1[x] is ancestors_2[x]:
                LCA = ancestors_1[x]
                x = x - 1
        except IndexError:
            pass
        
        return LCA