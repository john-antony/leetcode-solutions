# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            # if p and q is greater than curr.val check right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if p and q is less check left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # else we found our val return curr
            else:
                return curr
        

            
