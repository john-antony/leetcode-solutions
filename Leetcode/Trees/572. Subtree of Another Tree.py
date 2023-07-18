# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        # if same tree return true.
        if self.sameTree(root, subRoot):
            return True
        # return true if subRoot is atleast one of the subtrees of root.
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        #both root and subroot are empty
        if not root and not subRoot:
            return True
        # both root and subroot are non-empty so we compare them                
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        # one root is empty and the other is non-empty so we return False
        return False
