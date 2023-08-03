# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive approach: 
        # res = []
        # def preorder(root):
        #     if not root:
        #         return []
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)

        # return res

        # iterative approach with LIFO stack

        if not root:
            return []
        
        res, curr, stack = [], root, []

        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
                
            else:
                curr = stack.pop()
        
        return res
                

            

